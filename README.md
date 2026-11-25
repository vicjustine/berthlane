# berthlane

Three independent terminal services in one repository.

| Service | Responsibility | Tests |
|---|---|---|
| `services/gatein` | Truck gate-in lane assignment | 4 |
| `services/yardmap` | Yard slot allocation | 4 |
| `services/railout` | Rail departure planning | 4 |

Each service is self-contained: its own `src/` and `tests/`, no shared
imports. A change to one does not affect the others — which is the point
of testing them selectively rather than all together.

## Tests

```
pytest services/gatein/tests -q
pytest services/yardmap/tests -q
pytest services/railout/tests -q
```
