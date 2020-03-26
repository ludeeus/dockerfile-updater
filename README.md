# Dockerfile updater action

_It might not be pretty, but it does a good enough job, this one is for the lazy maintainer._

This will scan your repository for dockerfiles and update pinned versions in them, so you as a maintainer can just sit back and merge PR's.

If an update is found, that will be committed to a new branch and a pull request will be opened.

**Until I publish a 0.1.0 version you should probably not use this, I will continue messing with the code and use the action in this repository, as well as in [ludeeus/container](https://github.com/ludeeus/container)**


## Configuration options

Key | Optional | Default | Description
-- | -- | -- | --
`token` | False |  | GitHub token to use in the action `${{ secrets.GITHUB_TOKEN }}`
`pr_title` | True | `Dockerfile updates 🎉` | The title of the PR's this action creates.
`dockerfile_name` | True | `dockerfile` | This action run on all files that contains this value.
`exclude_type` | True |  | A comma separated string of types you don't want to check
`exclude_package` | True | | A comma separated string of packages you don't want to check
`commit_msg` | True | `"Update [package] from [from_version] to [to_version]"` | The string used in commit messages.

### Valid types for `exclude_type`

Type | Description
-- | --
`base` | For base image updates
`apk` | For alpine package updates
`pip` | For PyPi pacakge updates

## Recommended action configuration

_It is recommended to run this action with a cron trigger._

```yaml
name: Update Dockerfiles

on:
  schedule:
    - cron:  '40 16 * * *'
jobs:
  deploy:
    name: Update Dockerfiles
    runs-on: ubuntu-latest
    steps:
      - name: Checkout files
        uses: actions/checkout@master
      - name: Update Dockerfiles
        uses: ludeeus/dockerfile-updater@master
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
```

_This will run 4:40 PM every day._

## What is updated now

- Your base image (FROM) if you use `alpine` / `debian`
- Packages from PyPi.
- Alpine packages you install with `apk add`

## Planed for the future

- Debian packages you install with `apt install`
- More base images.
- Special ARG/ENV variables, (like `ARG S6_OVERLAY="vX.X.X"`).

***

_This project is made with [alpinepkgs](https://pypi.org/project/alpinepkgs), [PyGithub](https://pypi.org/project/PyGithub), [🍺/☕️](https://www.buymeacoffee.com/ludeeus) and [❤️](https://github.com/sponsors/ludeeus)_