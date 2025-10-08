# Annotation Rationale

These guidelines describe the decision criteria used during the manual annotation of software identity pairs for the Software Identity Resolution Benchmark.

The goal of this document is to allow future users of the data to understand how ambiguous or borderline cases were handled.


## Annotation labels

| Label	| Meaning |
|-------|---------|
| same |	Both repositories refer to the same software, even if hosted separately. |
| different |	The repositories represent distinct software projects. |
| unclear |	There is insufficient evidence to determine the relationship. These cases will be revisited when more data is available. |



## Common scenarios and how to annotate

### Clearly different projects — different

**Description**:
The repositories have distinct goals, codebases, or branding.

**Indicators**: 
- Different names and purposes.
- No shared contributors or versioning.
- Separate user communities.

**Decision**: different


### Forks as continuations — same

**Description**:
The forked repository is a clear continuation of the original project.

**Indicators**: 
- The fork starts where the original left off (e.g. original ends at v3.13, fork continues with v3.14+).
- Maintainers overlap significantly.
- Commit messages or README indicate continuity.
- No rebranding or major repurposing.

**Decision**: `same`


### Derived but Diverging — derived

**Description:**
One repo is inspired by or based on the other, but it represents a different project due to divergence in goal, name, or development team.

**Indicators:** 
- The fork becomes a new project (e.g. rebranded, new scope).
- Clear divergence in features or ideology.

**Decision:** `different`


### Independent reimplementations — `different`

**Description:**  
A new software is developed **from scratch** (not a fork), implementing similar or identical functionality to an existing one, often to address limitations, improve performance, or adapt to a new context. It may be accompanied by a **separate academic publication**.

**Indicators:**
- No code lineage (i.e., not a fork or clone).
- Independent citation/publication or author team.
- Different repository and codebase structure.
- May mention the original software as motivation or comparison.
- Often uses a different license, language, or design paradigm.

**Decision:** `different`


### Ambiguous forks — unclear

**Description**:
The fork has commits but does not clearly indicate if it’s a continuation, an experiment, or diverging.

**Indicators**: 
- No releases/tags in the fork.
- Minimal or no documentation.
- Unknown contributor relationship.
- No rebranding or changes in purpose, but no continuity signal either.

**Decision**: `unclear`


