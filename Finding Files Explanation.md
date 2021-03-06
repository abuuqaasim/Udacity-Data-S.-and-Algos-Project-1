## Finding Files

For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with a `“.c"` extension.

There are two solutions to this problem in the code. The first uses recursion to traverse the file hierarchy tree while building a path. The second uses Python’s `OS walk` method to build a path. The `OS walk` method was also tested and verified, but its test output is not included. Since there are no limit to the depth of the subdirectories can be, a recursive solution seemed like the natural approach. To test the code a couple directories were created aside from the Udacity supplied directory. These directories are included in the submission folder.

Time complexity is `O(#of terminal nodes in the file hierarchy tree)` The space complexity is `O(#of files with the desired extension)`.