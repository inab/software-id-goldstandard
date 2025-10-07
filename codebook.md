# Codebook – Software Identity Resolution Gold Standard
This codebook summarizes the fields in the gold‑standard annotation dataset for the **Software Identity Resolution Benchmark**.
**Sheet:** `Full annotation`

## Pair-level fields
| Field | Type | Allowed values / format | Description | Example |
|---|---|---|---|---|
| `entry_id` | `string` | – | Pair identifier used in the benchmark. | `slimfastq/*` |
| `human_decision` | `string` | same / unclear / different | Final adjudicated identity decision for the pair. | `same` |
| `human_confidence` | `string` | low / medium / high | Confidence category for the decision. | `high` |
| `human_rationale` | `string` | – | Short free-text justification for the decision. | `Same sourceforge page and descriptions refer to the same function` |
| `hard` | `string` | True / False | Whether the decision was hard to make. | `False` |

## Per-entry fields (applies to `entry_1_*` and `entry_2_*`)
For each **i ∈ {1, 2}**, the following fields exist; the full field name is `entry_i_<base>`.

| Base name | Full field | Type | Allowed values / format | Description | Example |
|---|---|---|---|---|---|
| `authors` | `entry_i_authors` | `string` | – | Maintainer/author/owner information for entry i (often `"Name" <email>`; possibly multiline). | `Bisong Yue <zhaokelei@cdu.edu.cn>
Kelei Zhao <bsyue@scu.edu.cn>` |
| `description` | `entry_i_description` | `string` | – | Free-text description/summary for entry i (may be multiline). | `Slimfastq is a cli application that compresses/decompresses fastq files.
It f…` |
| `id` | `entry_i_id` | `string` | – | Identifier string for entry i. | `sourceforge/slimfastq/None/None` |
| `license` | `entry_i_license` | `string` | GPL / MIT / LGPL / Custom / unknown / Apache-2.0 / BSD License / CC-BY-NC-2.0 / GPL-3.0-only / Artistic License | Software license for entry i (name or SPDX where available). | `Apache-2.0` |
| `name` | `entry_i_name` | `string` | – | Software/package name as given by the source for entry i. | `slimfastq` |
| `publication` | `entry_i_publication` | `string` | – | Publication reference associated with entry i (free text or identifier). | `` |
| `repository` | `entry_i_repository` | `string` | – | Repository or registry URL for entry i. | `https://sourceforge.net/projects/slimfastq` |
| `source` | `entry_i_source` | `string` | galaxy / biotools / toolshed / sourceforge / bioconda_recipes | Originating source/registry of entry i. | `sourceforge` |
| `type` | `entry_i_type` | `string` | db / cmd / lib / web / soap / undefined / workbench | Software type for entry i. | `undefined` |
| `webpage` | `entry_i_webpage` | `string` | – | Project webpage URL for entry i. | `https://slimfastq.sourceforge.io/` |

---
**Notes**

- Empty cells in the original spreadsheet are stored as `null` in the JSONL export.
- If you update column names in the Excel, regenerate the JSONL and revise this codebook accordingly.
- Enumerations shown in **Allowed values** are derived from known label sets or inferred when the column has a small number of distinct short values.
