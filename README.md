# Software Id Resolution benchmark – Gold Standard

This repository contains the gold-standard annotations used to evaluate software metadata identity resolution in life sciences.

## Contents

```
data/
  annotations.xlsx         # Canonical, human-friendly annotations (source of truth) / xlsx format
  annotations.ods          # Canonical, human-friendly annotations (source of truth) / ods format
  annotations.jsonl        # Machine-friendly export (one JSON object per line)
schema.json                # JSON Schema for each JSONL record
codebook.md                # Human-readable description of the dataset 
convert_xlsx_to_jsonl.py   # Reproducible converter from XLSX → JSONL
validate.py.               # little script to validate JSONL records
annotation_rationale.md    # decision criteria used during the annotation
```

## Generating the JSONL dataset

The canonical Excel file (`data/annotations.xlsx`) can be converted into a machine-readable JSONL file (`data/annotations.jsonl`) for downstream processing, benchmarking, or validation.
1.	Install the dependencies
    ```py
    pip install pandas openpyxl
    ```
2. Run the conversion script
    ```bash
    python convert_xlsx_to_jsonl.py --infile data/annotations.xlsx --outfile data/annotations.jsonl
    ```
3.	Output
The resulting file will contain one JSON object per line, with:
   - Column names normalized to snake_case.
   - Empty cells converted to null.
   - Date/time fields formatted as ISO-8601 strings.
1. Validate the generated file
To confirm that the conversion completed successfully and that the resulting JSONL file conforms to the expected structure, validate it against the provided schema:
    ```py
    pip install jsonschema
    python validate.py
    ```
The script will report any schema violations or confirm that all records comply with `schema.json`.


## License

This repository uses a dual-licensing model:

- **Data** (`data/annotations.xlsx`, `data/annotations.ods`, `data/annotations.jsonl`)  
  © 2025 Spanish National Bioinformatics Institute. Released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.  
  You are free to share and adapt the dataset provided appropriate credit is given.

- **Code and configuration** (`convert_xlsx_to_jsonl.py`, `schema.json`, `validate.py`)  
  Released under the **MIT License**.  
  You are free to use, modify, and redistribute the code with attribution.
