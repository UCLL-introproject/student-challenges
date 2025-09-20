# Semantic Versioning

When you're working on a software project, you often rely on code written by others to avoid having to write everything from scratch.
This code is provided as *packages*: these contain code that implement related functionality.
A few examples of Python packages:

* [Pygame](https://www.pygame.org/): offers all kinds of functionality useful to games (graphics, sound, math, efficient algorithms, ...)
* [Pillow](https://pypi.org/project/pillow/): imaging library.
* [Pytorch](https://pytorch.org/): machine learning library, can offload heavy computations to your GPU.
* [Click](https://click.palletsprojects.com/en/stable/): to easily build command line interfaces.
* [FastAPI](https://fastapi.tiangolo.com/): quickly build REST APIs.

Whenever your project relies on external packages, these are called *dependencies*.
Many programming languages come with a way to easily manage these dependencies, these tools are called *package managers*.
For example,

* JavaScript/TypeScript: npm, yarn, ...
* Python: pip, Poetry
* Ruby: Bundler
* Rust: Cargo
* Java: Maven, Gradle
* C#: NuGet

Packages get updated all the time.
Some of these updates fix bugs, other add new functionality.
As you develop your own project, it does make sense to also use the latest version of each of your dependencies.
However, it is also possible that an update will break your code, for any number of reasons.

For this reason, when you choose to add package as a dependency to your project, its version is also stored.
When someone else wants to work on or use your project, they will know which exact version of each of the dependencies to download.

You can always update your dependencies to the latest version, but that entails a risk.
It is crucial to thoroughly test your project to ensure nothing broke.

To help you assess the risk associated with updating a dependency, packages can use semantic versioning.
Semantic versioning represents a version using three numbers: `major`.`minor`.`patch`.

For example, say people are working on such a package, its current version being `4.2.8`.
Depending on the change they make, the version will be affected as follows:

* If the new changes are expected to break projects that rely on it, the `major` part is incremented.
  The new version number will be `5.0.0`.
* If new features were added, but they are not expected to break existing code, the `minor` part is incremented.
  In this case, the version goes from `4.2.8` to `4.3.0`.
* If the only changes are bug fixes, the `patch` part gets incremented, i.e., `4.2.9`.

Note that you should think in terms of risks, not certainties:
when a dependency only has its `minor` number go up, it is not a *guarantee* that your own code will keep working.
There can always be some unforeseen detail that causes things to break.
The only thing a minor version upgrade means, is that as far as the author is aware, there should be no breaking changes.
A `patch` version update should be seen as low risk (and not as no risk), a `minor` update as medium risk and `major` update as high risk.

## Question

Below are given a few version numbers that following the semantic version scheme.
Determine what the new version number should be for each, based on the type of update.
Next order these version numbers from old to new, e.g., version 1.5.0 is older than 3.1.4.

* `1.9.5` minor update
* `1.2.4` major update
* `4.9.9` patch update
* `2.1.7` minor update
* `2.2.2` patch update
