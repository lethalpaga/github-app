#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import github


if __name__ == '__main__':
    import pprint
    
    app = github.GitHubApp()
    installation = app.get_installation(os.environ['GITHUB_ORG'])
    pprint.pprint(installation.get_repositories())

    pprint.pprint(app)
