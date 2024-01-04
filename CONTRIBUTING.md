# Contributing to NumInsight

First off, thank you for considering contributing to NumInsight. It's people like you that make NumInsight such a great tool.

## Where do I go from here?

If you've noticed a bug or have a feature request, make the first move by creating an issue in the GitHub repository. That's the first step to contributing to NumInsight!

## Fork & create a branch

If this is something you think you can fix, then fork the repository and create a branch with a descriptive name.

A good branch name would be (where issue #325 is the ticket you're working on):

```bash
git checkout -b feature/325-add-japanese-localization
```

## Implement your fix or feature

At this point, you're ready to make your changes! Feel free to ask for help; everyone is a beginner at first.

## Write a good commit message

A good commit message serves at least three important purposes:

- To speed up the reviewing process.
- To help us write a good release note.
- To help the future maintainers of NumInsight (it could be you!), say five years into the future, to find out why a particular change was made to the code or why a specific feature was added.

Here's an example of a good commit message:

```bash
git commit -m "[ADD] Added Japanese localization - fixes #325"
```

## Submit a pull request

Push your branch to your fork on GitHub, then press the `New pull request` button, and you are good to go!

It's generally a good idea to have a PR's content cover exactly one specific issue, and to have a reference to that issue in the description of your pull request.

## Keeping your Pull Request updated

If a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update your branch so it's easier to merge.

To learn more about rebasing in Git, there are a lot of good [resources](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) but here's the suggested workflow:

```bash
git checkout feature/325-add-japanese-localization
git pull origin main
git rebase main
git push --force-with-lease origin feature/325-add-japanese-localization
```


# Thank you again for your contribution!
