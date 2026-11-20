# Model selection

Fill this in after you have trained your candidates in MLflow. Short sentences are fine. Use numbers from your runs.

## The question
What does this model decide, and who is hurt by a wrong answer? (One or two sentences.)

## Candidates
| Candidate | Why I tried it | AUC | F1 | F1 per slice (lowest) | p95 latency (ms) | Size (KB) | MLflow run ID |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

## The champion
Which one did I pick, and what decided it? (Name the numbers that mattered and the ones I accepted losing.)

## My promotion rules
- Latency budget (p95): ___ ms, because ___
- Minimum gain to replace the champion (F1 points): ___, because ___

## What I would check next
One thing that could make this choice wrong in production (for example a slice with few customers, or data that changes).
