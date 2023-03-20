# Assetto Corsa dammy Python library
Dummy library for Assetto Corsa native functions presented in Python.

Actually, it has a single interface for `ac` module.

The main goal of this package: provide convenient autocomplete in IDE (tested in PyCharm).

## Installation to develop AC mod

You will need to install the package:
```shell
pip install AcDummyLib
```

Add following in your script instead of `import ac`:
```python
if __name__ == '__main__':
    ### pip install AcDummyLib
    from AcDummyLib import ac
else:
    import ac
```

Now you can check your IDE, autocomplete shall work.

## Contribution
You are very welcome to add changes into this code. =)
Please feel free to push merge/pull requests.

Or, you may raise an issue to highlight found discrepancies.

## Roadmap

- Migrate function descriptions into the interface file.

## References

#### Source documents:
- https://docs.google.com/document/d/13trBp6K1TjWbToUQs_nfFsB291-zVJzRZCNaTYt4Dzc/pub
- https://assettocorsamods.net/attachments/inofficial_acpythondoc_v2-pdf.7415/

#### Initial forum threads:
- https://assettocorsamods.net/threads/doc-python-doc.59
- https://assettocorsamods.net/threads/is-there-a-way-to-load-ac-library-to-have-autocomplete-in-an-ide-e-g-pycharm.3088/