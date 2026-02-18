## Status: Proof of Concept 

This repository was used to validate Python → MetaCall → TypeScript
integration for MCP.

Findings:
- Python ↔ JS argument marshaling works correctly.
- metacall/protocol can be driven externally.
- MetaCall Python bindings currently do not support awaiting JS Promises,
  which blocks async protocol usage.

As a result, the MCP implementation was moved to TypeScript.
