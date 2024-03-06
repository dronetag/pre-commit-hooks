# pre-commit-hooks

Specific hooks for dronetag

### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/dronetag/pre-commit-hooks
    rev: v1.0.0
    hooks:
    -   id: check-email-domain
```

### Hooks available

#### `check-email-domain`
Checks that commiter's email has correct domain. Put allowed domains into `args: [yourdomain.com]` or `args: [yourdomain.com, otherdomain.com]`.
