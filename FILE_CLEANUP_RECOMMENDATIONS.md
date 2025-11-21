# File Cleanup Recommendations for v2.0

This document provides recommendations for which files can be archived or deleted after the migration to Anthropic Agent SDK (v2.0).

---

## 📊 Summary

- **Total Files Analyzed:** 31
- **✅ Keep (Required):** 17 files
- **⚠️ Update Needed:** 2 files
- **📦 Archive (Obsolete but historical):** 7 files
- **🗑️ Delete (No longer relevant):** 5 files

---

## ✅ KEEP - Essential Files (17)

### Core System Files
| File | Purpose | Status |
|------|---------|--------|
| `strategy_consulting_agent.py` | Updated legacy mode (Anthropic-compatible) | ✅ Active |
| `orchestrator.py` | New SDK-based orchestrator | ✅ Active |
| `prompt_manager.py` | YAML prompt management (still used) | ✅ Active |
| `agent_prompts.yaml` | Prompt configuration (still used) | ✅ Active |
| `requirements.txt` | Dependencies (updated for Anthropic) | ✅ Active |

### Configuration Files
| File | Purpose | Status |
|------|---------|--------|
| `.gitignore` | Git ignore rules | ✅ Active |
| `env_example.txt` | Environment variable template | ✅ Updated for Anthropic |
| `activate_env.sh` | Virtual environment activation | ✅ Active |

### Subagent Definitions (New in v2.0)
| File | Purpose | Status |
|------|---------|--------|
| `.claude/agents/business-model-analyst.md` | Subagent definition | ✅ Active |
| `.claude/agents/market-researcher.md` | Subagent definition | ✅ Active |
| `.claude/agents/competitive-analyst.md` | Subagent definition | ✅ Active |
| `.claude/agents/financial-analyst.md` | Subagent definition | ✅ Active |
| `.claude/agents/risk-assessor.md` | Subagent definition | ✅ Active |
| `.claude/agents/implementation-specialist.md` | Subagent definition | ✅ Active |
| `.claude/agents/strategy-storyteller.md` | Subagent definition | ✅ Active |
| `.claude/agents/senior-partner.md` | Subagent definition | ✅ Active |
| `.claude/settings.local.json` | Claude Code settings | ✅ Active |

---

## ⚠️ UPDATE NEEDED - Files That Need Updating (2)

### 1. `README.md` ⚠️ NEEDS UPDATE
**Current Status:** Still references v1.0 (OpenAI-based system)

**What Needs Updating:**
- Add section about v2.0 and Anthropic migration
- Update installation instructions to include `ANTHROPIC_API_KEY`
- Add section about two execution modes (legacy vs SDK)
- Update usage examples to show both modes
- Add link to `MIGRATION_TO_ANTHROPIC.md`

**Recommendation:** Update with v2.0 information

---

### 2. `SETUP_README.md` ⚠️ NEEDS UPDATE
**Current Status:** Setup instructions still reference OpenAI

**What Needs Updating:**
- Update API key setup instructions (ANTHROPIC_API_KEY)
- Add note about backward compatibility
- Update dependency list if needed

**Recommendation:** Update for v2.0

---

## 📦 ARCHIVE - Obsolete but Keep for Historical Reference (7)

These files are no longer used in v2.0 but contain historical context about the system's evolution. Move to an `archive/` directory.

### 1. `MIGRATION_SUMMARY.md` 📦 ARCHIVE
**Why:** Documents the OLD migration (hardcoded → YAML prompts)
**Superseded by:** `MIGRATION_TO_ANTHROPIC.md`
**Historical value:** Shows evolution from v0 → v1.0
**Recommendation:** Move to `archive/v1.0/MIGRATION_SUMMARY.md`

---

### 2. `PROMPT_CONFIG_README.md` 📦 ARCHIVE OR UPDATE
**Why:** Documents YAML prompt system (still relevant) but references GPT-5
**Options:**
- **Option A:** Update to mention it's still used in legacy mode
- **Option B:** Archive with note that this is for v1.0 YAML system
**Recommendation:** Move to `archive/v1.0/` or update with v2.0 notes

---

### 3. `example_usage.py` 📦 ARCHIVE
**Why:** Uses OpenAI API (`OPENAI_API_KEY`)
**Status:** Outdated for v2.0, but shows legacy usage patterns
**Recommendation:**
- Archive to `archive/v1.0/example_usage.py`
- Create new `example_usage_v2.py` showing orchestrator usage

---

### 4. `test_agent_execution.py` 📦 ARCHIVE
**Why:** Tests using `OPENAI_API_KEY`
**Status:** Legacy v1.0 testing
**Recommendation:** Move to `archive/v1.0/tests/`

---

### 5. `test_consulting_team.py` 📦 ARCHIVE
**Why:** Tests using `OPENAI_API_KEY`
**Status:** Legacy v1.0 testing
**Recommendation:** Move to `archive/v1.0/tests/`

---

### 6. `test_multi_agent.py` 📦 ARCHIVE
**Why:** Tests using `openai` package import
**Status:** Legacy v1.0 testing
**Recommendation:** Move to `archive/v1.0/tests/`

---

### 7. `test_pythonEnv.py` 📦 ARCHIVE
**Why:** Basic environment test (likely outdated)
**Status:** May be obsolete
**Recommendation:** Review and archive if not needed

---

## 🗑️ DELETE - No Longer Relevant (5)

These files can be safely deleted as they serve no purpose in v2.0 and have no historical value worth preserving.

### 1. `debug_api_call.py` 🗑️ DELETE
**Why:** Specifically tests OpenAI API calls
**Code:** Hardcoded to use `openai` client and `OPENAI_API_KEY`
**Reason to delete:** Debugging script for old API, not relevant
**Recommendation:** ✅ DELETE

---

### 2. `update_agents_to_prompt_manager.py` 🗑️ DELETE
**Why:** Migration script from hardcoded prompts to YAML
**Status:** One-time migration already completed
**Reason to delete:** Migration tool no longer needed
**Recommendation:** ✅ DELETE

---

### 3. `setup_project.py` 🗑️ DELETE OR UPDATE
**Why:** Checks for `openai` package specifically
**Current behavior:** Will fail on v2.0 since we use `anthropic`
**Options:**
- **Delete:** If not used
- **Update:** Change to check for `anthropic` package
**Recommendation:** ✅ DELETE (or update if actively used)

---

### 4. `test_installation.py` 🗑️ DELETE
**Why:** Tests for `openai` package import
**Status:** Will fail in v2.0 environment
**Reason to delete:** Needs complete rewrite for Anthropic
**Recommendation:** ✅ DELETE (or rewrite for v2.0)

---

### 5. `test_prompt_manager.py` ⚠️ REVIEW BEFORE DELETING
**Why:** Tests the prompt_manager.py functionality
**Status:** Prompt manager still used in legacy mode
**Reason to keep:** May still be useful for legacy mode testing
**Recommendation:** ⚠️ KEEP (prompt manager still used)

---

## 📁 Recommended Directory Structure After Cleanup

```
consulting-agents/
├── .claude/
│   └── agents/                          # ✅ KEEP - v2.0 subagents
│       ├── business-model-analyst.md
│       ├── market-researcher.md
│       └── ... (6 more)
├── archive/
│   └── v1.0/                            # 📦 NEW - Historical files
│       ├── MIGRATION_SUMMARY.md
│       ├── PROMPT_CONFIG_README.md
│       ├── example_usage.py
│       └── tests/
│           ├── test_agent_execution.py
│           ├── test_consulting_team.py
│           └── test_multi_agent.py
├── docs/                                # 📦 NEW - Documentation
│   ├── MIGRATION_TO_ANTHROPIC.md       # ✅ v2.0 migration guide
│   ├── PHASE_1_2_SUMMARY.md            # ✅ v2.0 summary
│   └── SETUP_README.md                 # ⚠️ UPDATE for v2.0
├── orchestrator.py                      # ✅ KEEP - v2.0 orchestrator
├── strategy_consulting_agent.py        # ✅ KEEP - Updated legacy mode
├── prompt_manager.py                    # ✅ KEEP - Still used
├── agent_prompts.yaml                   # ✅ KEEP - Still used
├── requirements.txt                     # ✅ KEEP - Updated
├── env_example.txt                      # ✅ KEEP - Updated
├── README.md                            # ⚠️ UPDATE for v2.0
└── test_prompt_manager.py              # ✅ KEEP - Still relevant
```

---

## 🚀 Action Plan

### Phase 1: Create Archive Directory
```bash
mkdir -p archive/v1.0/tests
```

### Phase 2: Move Files to Archive
```bash
# Historical documentation
mv MIGRATION_SUMMARY.md archive/v1.0/
mv PROMPT_CONFIG_README.md archive/v1.0/
mv example_usage.py archive/v1.0/

# Old test files
mv test_agent_execution.py archive/v1.0/tests/
mv test_consulting_team.py archive/v1.0/tests/
mv test_multi_agent.py archive/v1.0/tests/
mv test_pythonEnv.py archive/v1.0/tests/
```

### Phase 3: Delete Obsolete Files
```bash
# Migration/debug tools
rm debug_api_call.py
rm update_agents_to_prompt_manager.py
rm setup_project.py  # or update if needed
rm test_installation.py
```

### Phase 4: Update Documentation
```bash
# Update these files with v2.0 information
# - README.md (add v2.0 section)
# - SETUP_README.md (update API key instructions)
```

### Phase 5: Optional - Create New Docs Directory
```bash
mkdir -p docs
mv MIGRATION_TO_ANTHROPIC.md docs/
mv PHASE_1_2_SUMMARY.md docs/
```

---

## 📋 Quick Reference Table

| File | Action | Destination | Reason |
|------|--------|-------------|--------|
| `.claude/agents/*.md` | ✅ Keep | Current location | New v2.0 subagents |
| `orchestrator.py` | ✅ Keep | Current location | New v2.0 orchestrator |
| `strategy_consulting_agent.py` | ✅ Keep | Current location | Updated for Anthropic |
| `README.md` | ⚠️ Update | Current location | Add v2.0 info |
| `SETUP_README.md` | ⚠️ Update | Current location | Update API key |
| `MIGRATION_SUMMARY.md` | 📦 Archive | `archive/v1.0/` | Historical |
| `PROMPT_CONFIG_README.md` | 📦 Archive | `archive/v1.0/` | Historical/legacy |
| `example_usage.py` | 📦 Archive | `archive/v1.0/` | Uses OpenAI |
| `test_agent_execution.py` | 📦 Archive | `archive/v1.0/tests/` | Legacy tests |
| `test_consulting_team.py` | 📦 Archive | `archive/v1.0/tests/` | Legacy tests |
| `test_multi_agent.py` | 📦 Archive | `archive/v1.0/tests/` | Legacy tests |
| `test_pythonEnv.py` | 📦 Archive | `archive/v1.0/tests/` | Legacy tests |
| `debug_api_call.py` | 🗑️ Delete | - | OpenAI debug only |
| `update_agents_to_prompt_manager.py` | 🗑️ Delete | - | One-time migration |
| `setup_project.py` | 🗑️ Delete | - | Checks for OpenAI |
| `test_installation.py` | 🗑️ Delete | - | Checks for OpenAI |
| `test_prompt_manager.py` | ✅ Keep | Current location | Still relevant |

---

## 🎯 Recommended Actions

### Immediate (Before Next Commit)
1. ✅ Delete obsolete files that have no historical value
2. 📦 Move legacy files to `archive/v1.0/`
3. ⚠️ Update `README.md` with v2.0 information

### Short-term (Next 1-2 weeks)
4. Create new `example_usage_v2.py` showing orchestrator usage
5. Create new test suite for v2.0 (orchestrator and Anthropic API)
6. Update `SETUP_README.md` for v2.0

### Optional Enhancements
7. Reorganize docs into `docs/` directory
8. Create `CONTRIBUTING.md` for v2.0 development
9. Add `CHANGELOG.md` documenting v1.0 → v2.0 changes

---

## ⚠️ Important Notes

1. **Don't delete `prompt_manager.py` or `agent_prompts.yaml`** - These are still used by the legacy mode (`strategy_consulting_agent.py`)

2. **Keep backward compatibility** - The legacy mode (`strategy_consulting_agent.py`) should continue to work for users who prefer it

3. **Preserve historical context** - Archive rather than delete files that show the evolution of the system

4. **Test before deleting** - Ensure nothing depends on the files marked for deletion

---

**Last Updated:** November 20, 2025 (v2.0 Migration)
**Status:** Ready for Review and Implementation
