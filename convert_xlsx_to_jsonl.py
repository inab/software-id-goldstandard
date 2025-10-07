#!/usr/bin/env python3
"""
Convert the canonical Excel annotations to normalized JSONL for the benchmark.

- Input: data/annotations.xlsx (first sheet by default, configurable via --sheet)
- Output: data/annotations.jsonl

Normalization:
- Columns are converted to snake_case.
- NaNs/empty strings become null.
- Datetimes are converted to ISO 8601 strings.
"""

import argparse
import json
import pathlib
import sys

import pandas as pd


def to_snake(s: str) -> str:
    return "_".join(
        str(s)
        .strip()
        .replace("\n", " ")
        .replace("/", " or ")
        .replace("-", " ")
        .replace(".", " ")
        .lower()
        .split()
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--infile", default="data/annotations.xlsx")
    ap.add_argument("--sheet", default=None, help="Excel sheet name (default: first sheet)")
    ap.add_argument("--outfile", default="data/annotations.jsonl")
    args = ap.parse_args()

    xls = pd.ExcelFile(args.infile)
    sheet = args.sheet or xls.sheet_names[0]
    df = pd.read_excel(args.infile, sheet_name=sheet)

    # normalize columns
    col_map = {c: to_snake(c) for c in df.columns}
    df = df.rename(columns=col_map)

    # convert datetimes to ISO8601 strings
    for c in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[c]):
            df[c] = df[c].dt.strftime("%Y-%m-%dT%H:%M:%S%z").str.replace("+0000", "+00:00")

    # write jsonl
    outp = pathlib.Path(args.outfile)
    outp.parent.mkdir(parents=True, exist_ok=True)
    with outp.open("w", encoding="utf-8") as f:
        for _, row in df.iterrows():
            obj = {k: (None if (pd.isna(v) or str(v).strip() == "") else v) for k, v in row.items()}
            json.dump(obj, f, ensure_ascii=False)
            f.write("\n")

    print(f"Wrote {outp}")
    return 0


if __name__ == "__main__":
    sys.exit(main())