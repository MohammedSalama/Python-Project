def disconnect_github(access_token, repo_hooks):
    """Uninstall webhooks."""
    # Note at this point the remote account and all associated data have
    # already been deleted. The celery task is passed the access_token to make
    # some last cleanup and afterwards delete itself remotely.
    import github3
    from .api import GitHubAPI

    try:
        gh = github3.login(token=access_token)
        for repo_id, repo_hook in repo_hooks:
            ghrepo = gh.repository_with_id(repo_id)
            if ghrepo:
                hook = ghrepo.hook(repo_hook)
                if hook and hook.delete():
                    info_msg = u'Deleted hook {hook} from {repo}'.format(
                        hook=hook.id, repo=ghrepo.full_name)
                    current_app.logger.info(info_msg)
        # If we finished our clean-up successfully, we can revoke the token
        GitHubAPI.revoke_token(access_token)
    except Exception as exc:
        # Retry in case GitHub may be down...
        disconnect_github.retry(exc=exc) 
