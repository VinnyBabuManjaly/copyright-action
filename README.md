# 🚀 Copyright Action

Github Action for automatically inserting copyright notice to the configured directories in a repository.

## Usage

Basic:
```yaml
steps:
- uses: actions/checkout@v2
- uses: VinnyBabuManjaly/copyright-action@master
  with:
    CopyrightString: 'Copyright check\nAll rights reserved (c)\n'
    FileType: '.py, .txt'
    Path: 'testfolder1/, testfolderb'
    IgnorePath: 'testfolderc/a/, testfolderc/b'
```
See [action.yml](action.yml) for more details.

### Input variables

|| Description | Syntax | Example |
|------|-------|-------|-------|
| **CopyrightString** (Required)| String to be added as copyright notice(multiline copyrights are possible). | Copyright notice string multi line or single line seperated '\n'(new line) in single quotes. | `'Copyright check\nAll rights reserved (c)\n'` |
| **FileType** (Required) | Type of files(extension) for which copyright notice has to be added in the given file path. | File extensions seperated by ','(comma) in single quotes. | `'.py, .txt'` |
| **Path** (Optional) | Path in which copyright notice has to be added to files. | Directories ending with or without '/'(slash) seperated by ','(comma) in single quotes. | `'testfolder1/, testfolderb'` |
| **IgnorePath** (Optional) | Path ignored without adding copyright notice. | Directories ending with or without '/'(slash) seperated by ','(comma) in single quotes. | `'testfolderc/a/, testfolderc/b'` |

## License

The scripts and documentation in this project are released under the [MIT License](LICENSE).

## Contributions

Contributions are welcome!
Please submit a pull request for any improvements on the action.
If you experience issues using this action in your workflow, submit an issue describing changes you may require.
