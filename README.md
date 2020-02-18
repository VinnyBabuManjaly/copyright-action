# 🚀 Copyright Action

Github Action for automatically inserting copyright notice to the configured directories in a repository and creates a pull request for the same.

Additionally, if the copyright notice is already present in a file/files in configured directories, the action is skipped without modifying the file content. Also, for the empty files, its skipped. And if wrong directory is specified and no files are found matching, according to the given parameters in any of the specified directories, warning message is displayed in the logs.

## Usage

Basic:
```yaml
steps:
  # Checking out the repository which is to be actioned
  - uses: actions/checkout@v2
  # Implementing action on repository
  - uses: VinnyBabuManjaly/copyright-action@master
    with:
      CopyrightString: 'Copyright check\nAll rights reserved (c)\n'
      FileType: '.py, .txt'
      Path: 'testfolder1/, testfolder2'
      IgnorePath: 'testfolder1/a/, testfolder3'
  # Creates pull request with all changes in file
  - name: Create Pull Request
    uses: peter-evans/create-pull-request@v2
    with:
      token: ${{ secrets.GITHUB_TOKEN }}
```
See [action.yml](action.yml) for more details.

### Input variables

|| Description | Syntax | Example |
|------|-------|-------|-------|
| **CopyrightString** (Required)| String to be added as copyright notice(multiline copyrights are possible). | Copyright notice string multi line or single line seperated '\n'(new line) in single quotes. | `'Copyright check\nAll rights reserved (c)\n'` |
| **FileType** (Required) | Type of files(extension) for which copyright notice has to be added in the given file path. | File extensions seperated by ','(comma) in single quotes. | `'.py, .txt'` |
| **Path** (Optional) | Path in which copyright notice has to be added to files. | Directories ending with or without '/'(slash) seperated by ','(comma) in single quotes. | `'testfolder1/, testfolder2'` |
| **IgnorePath** (Optional) | Path ignored without adding copyright notice. | Directories ending with or without '/'(slash) seperated by ','(comma) in single quotes. | `'testfolder1/a/, testfolder3'` |

If the optional input **Path** is not given, it takes the all the directories present in the repository to be actioned.
Similarly **IgnorePath** is also an optional parameter, while **CopyrightString** and **FileType** are always required.

## License

The scripts and documentation in this project are released under the [MIT License](LICENSE).

## Contributions

Contributions are welcome!
Please submit a pull request for any improvements on the action.
If you experience issues using this action in your workflow, submit an issue describing changes you may require.
