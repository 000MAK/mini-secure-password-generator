# Mini Secure Password Generator

A Python command-line demonstration that generates random passwords using Python's `secrets` module rather than the standard pseudo-random module.

**Independent demonstration project** · Python 3.10+ · Standard library only · MIT license

## Features

- Uses cryptographically strong randomness through `secrets`.
- Supports password lengths from 12 to 128 characters.
- Includes letters, digits, and symbols by default.
- Offers a `--no-symbols` option.
- Prints the generated password once and does not save it automatically.

## Quick start

```bash
python main.py --help
python main.py --length 24
python main.py --length 20 --no-symbols
```

The default length is 20 characters. The program prints a reminder to store the result in a password manager.

## Tests

```bash
python -m unittest discover -s tests -v
```

## Security notes and limitations

This is a small password-generation example, not a complete credential-management system. Generated secrets appear in terminal output and may be retained by terminal logging, screen capture, or shell history in some environments. Avoid sharing screenshots or logs containing generated passwords, and store credentials in a reputable password manager. Review password policy requirements before use in a managed environment.

## Related Quantix projects

- [Mini Log Redactor](https://github.com/000MAK/mini-log-redactor)
- [Quantix — 100 Mini Python Projects](https://github.com/000MAK/quantix-100-new-mini-projects)

## License

MIT. See [LICENSE](LICENSE).
