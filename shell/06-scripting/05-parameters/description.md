# Parameters

Say we have the following script named `create-student-repo`:

```bash
#!/bin/sh

gh repo create --private UCLL-Project/r0123456 --clone
cd r0123456
git remote add upstream git@github.com:UCLL-Project/starter-code.git
git pull upstream main
git push -u upstream main
gh issue create --title "Perform task 1" --body "Description of task 1"
gh issue create --title "Perform task 2" --body "Description of task 2"
gh issue create --title "Perform task 3" --body "Description of task 3"
```

This script creates a new repository on GitHub for student `r0123456`, adds starter code to it, and creates three issues (=TODOs).
However, this script is hardcoded for one specific student, and we would like to generalize it so that we can type

```bash
./create-student-repo r1111111
```

and it will create a repository for student `r1111111` instead of for `r0123456`.
This can be achieved using parameters, i.e., the script should make use of the extra information (`r1111111`) we pass to it.

Copy this script to `solution.txt` and make minimal changes so that it can be used for arbitrary students.
