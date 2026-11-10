# Connectivity Diagnostics Lab

eSIM, SGP22/32, communications analysis, learning.

A personal Python laboratory for connectivity diagnostics, simulated eSIM operations and automated testing. Companion project to [eSIM Flow Atlas](https://github.com/JoseLuisMorenoVillanueva/eSIM_flow_atlas).

**Current scope:** one fictional event printed as JSON. This is not a network probe, a GSMA implementation or a conformance test. Use synthetic data only.

## Start here

Read [Week 1 — first session (Spanish)](docs/week-01.md).

### Codespaces

Open Code → Codespaces → Create codespace on main. The development container uses Python 3.12 and creates a local `.venv`. After setup:

```bash
.venv/bin/python src/first_event.py
```

No third-party Python packages are required. The image tag fixes the Python minor version and OS family, not an immutable image digest.

### Local Linux

Install Git and Python 3.12 with venv support, then:

```bash
git clone https://github.com/JoseLuisMorenoVillanueva/connectivity-diagnostics-lab.git
cd connectivity-diagnostics-lab
python3 -m venv .venv
.venv/bin/python src/first_event.py
```

If venv reports that ensurepip is unavailable on Mint, install your distribution's matching Python venv package and retry.

### Local Windows (PowerShell)

Install Git and Python 3.12, then:

```powershell
git clone https://github.com/JoseLuisMorenoVillanueva/connectivity-diagnostics-lab.git
cd connectivity-diagnostics-lab
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe src/first_event.py
```

Explicit interpreter paths avoid changing PowerShell execution policy.

### Local Dev Container (optional)

With Docker and the VS Code Dev Containers extension installed, open the repository and run **Dev Containers: Reopen in Container**. This uses the same configuration as Codespaces but executes on your computer. It is a Linux environment, including on a Windows host.

## Switching computers

Finish one session before editing the same branch elsewhere:

```bash
git status
git diff
git add src/first_event.py
git commit -m "Describe the change"
git push
```

Stage other intended files explicitly. Commit only when there are changes.
On the next computer, open the same branch with a clean working tree:

```bash
git pull --ff-only
```

If Git refuses, inspect `git status` and ask for help; do not force-push or discard changes.
Virtual environments and secrets do not travel with Git. Recreate the environment on each machine.
Stop the Codespace explicitly when finished; stopping compute does not remove stored files.

## Learning path

1. Environment, Git and one JSON event.
2. Generate and validate fictional events.
3. Analyze logs from a CLI.
4. REST client and a teaching API.
5. Tests, eSIM scenarios, networking, Docker and MQTT.

Future phases are exercises, not implemented features.

## Licensing

The original project code is provided under [PolyForm Noncommercial 1.0.0](LICENSE.md).
See [NOTICE](NOTICE) for attribution.

Noncommercial uses are permitted under the license's definitions, including its specified organizational uses. Uses outside that grant require separate permission from the rights holder. This is source-available software, not an unrestricted open-source license. Third-party tools retain their own licenses.

Publishing the repository allows people to view and download it; a license restricts authorized use, not technical copying.
