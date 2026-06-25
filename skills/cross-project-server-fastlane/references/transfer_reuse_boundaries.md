# Transfer Reuse Boundaries

Use this reference to keep server-transfer tooling reusable.

## Reusable

- Manifest shape: relpath, local path, server path, bytes, sha256.
- Missing-only and mismatch-only transfer policy.
- Server-side verification before launch.
- Runtime/import/model/cache probe pattern.
- Isolated output-root rule.
- Wrapper/status contract checks.
- Small summary pullback instead of large artifact pullback.
- BLOCK/HOLD/ALLOW launch decisions.

## Needs Project Configuration

- Local project root.
- Server project root.
- Transport mechanism: SSH, OSS queue, rclone, shared drive, object storage.
- Owner queue or remote workspace identity.
- Python/runtime path.
- GPU requirements.
- Large artifact storage policy.
- Finalizer/status command.

## Do Not Reuse Blindly

- Private bucket names, access keys, tokens, usernames.
- Machine-specific paths.
- Existing transfer logs.
- Project-specific runner scripts.
- Dataset or model claims.
