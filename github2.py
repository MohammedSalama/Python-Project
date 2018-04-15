def init_account(self):
        """Setup a new GitHub account."""
        ghuser = self.api.me()
        # Setup local access tokens to be used by the webhooks
        hook_token = ProviderToken.create_personal(
            'github-webhook',
            self.user_id,
            scopes=['webhooks:event'],
            is_internal=True,
        )
        # Initial structure of extra data
        self.account.extra_data = dict(
            id=ghuser.id,
            login=ghuser.login,
            name=ghuser.name,
            tokens=dict(
                webhook=hook_token.id,
            ),
            repos=dict(),
            last_sync=iso_utcnow(),
        )
        db.session.add(self.account)

        # Sync data from GitHub, but don't check repository hooks yet.
        self.sync(hooks=False) 
