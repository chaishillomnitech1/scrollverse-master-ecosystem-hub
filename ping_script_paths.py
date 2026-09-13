#!/usr/bin/env python3
"""
LOCAL SCRIPT DIRECTORY PATH VERIFIER
Strategy: Absolute Verification of Workspace Configuration Prior to Execution

This diagnostic tool confirms your workspace alignment before running commits.
Never assumes paths exist. Tests them and reports honestly.
"""

import os
import sys

# ==============================================================================
# CONFIGURATION: REQUIRED PATHS FOR SCROLLVERSE ECOSYSTEM
# ==============================================================================

REQUIRED_PATHS = {
    "Target Directory": "./archives/AI-LEGION-CREATIVE-CONVERGENCE",
    "Verification Engine": "./verify_repo_states.py",
    "Provenance Log Template": "./PROVENANCE-LOG-TEMPLATE.md",
    "Schema Machine-Readable": "./SCHEMA-MACHINE-READABLE.yaml",
    "Three-Layer Foundation": "./THREE_LAYER_FOUNDATION_SEALED.md",
    "Release Genesis Manifest": "./RELEASE_v1.0.0_MANIFEST.json",
    "Repository Root": "./"
}

OPTIONAL_PATHS = {
    "Config Directory": "./config",
    "Phase 68 Schema": "./config/phase68_registry_schema.json",
    "Provenance Report": "./provenance-audit-report.json"
}

# ==============================================================================
# CORE FUNCTIONS
# ==============================================================================

def get_absolute_path(relative_path):
    """
    Returns absolute path without assuming it exists.
    """
    return os.path.abspath(relative_path)

def check_path_status(path):
    """
    Returns detailed status of a path.
    Returns: (exists, is_dir, is_file, details)
    """
    if os.path.exists(path):
        if os.path.isdir(path):
            return (True, True, False, "Directory found")
        elif os.path.isfile(path):
            return (True, False, True, "File present")
        else:
            return (True, False, False, "Path exists (unknown type)")
    else:
        return (False, False, False, "Path not found (awaiting deployment)")

def verify_workspace_alignment():
    """
    Execute full workspace path verification.
    Report only actual observations. Mark unverified as PENDING.
    """
    
    print("\n" + "="*80)
    print("🛰️  LOCAL WORKSPACE PATH ALIGNMENT CHECK")
    print("="*80)
    print("\nStrategy: Absolute verification of workspace configuration")
    print("Status: Testing actual file system state (not assuming)\n")
    
    # ==== REQUIRED PATHS ====
    print("[CRITICAL PATHS - MUST EXIST]\n")
    
    required_aligned = True
    required_results = {}
    
    for label, path in REQUIRED_PATHS.items():
        abs_path = get_absolute_path(path)
        exists, is_dir, is_file, details = check_path_status(path)
        
        if exists:
            status_symbol = "✅"
            status_text = "ALIGNED"
        else:
            status_symbol = "❌"
            status_text = "MISALIGNED"
            required_aligned = False
        
        required_results[label] = {
            "path": path,
            "absolute_path": abs_path,
            "exists": exists,
            "is_directory": is_dir,
            "is_file": is_file,
            "status": status_text,
            "details": details
        }
        
        print(f"{status_symbol} **{label}**")
        print(f"   Path: {path}")
        print(f"   Status: {status_text}")
        print(f"   Details: {details}")
        print(f"   Absolute: {abs_path}")
        print()
    
    # ==== OPTIONAL PATHS ====
    print("\n[OPTIONAL PATHS - NICE TO HAVE]\n")
    
    optional_results = {}
    
    for label, path in OPTIONAL_PATHS.items():
        abs_path = get_absolute_path(path)
        exists, is_dir, is_file, details = check_path_status(path)
        
        if exists:
            status_symbol = "✅"
            status_text = "PRESENT"
        else:
            status_symbol = "⚠️ "
            status_text = "PENDING"
        
        optional_results[label] = {
            "path": path,
            "absolute_path": abs_path,
            "exists": exists,
            "is_directory": is_dir,
            "is_file": is_file,
            "status": status_text,
            "details": details
        }
        
        print(f"{status_symbol} **{label}**")
        print(f"   Path: {path}")
        print(f"   Status: {status_text}")
        print(f"   Details: {details}")
        print()
    
    # ==== SUMMARY ====
    print("\n" + "="*80)
    print("WORKSPACE ALIGNMENT SUMMARY")
    print("="*80)
    
    critical_count = len(REQUIRED_PATHS)
    critical_aligned = sum(1 for r in required_results.values() if r['exists'])
    optional_count = len(OPTIONAL_PATHS)
    optional_present = sum(1 for o in optional_results.values() if o['exists'])
    
    print(f"\nCritical Paths: {critical_aligned}/{critical_count} aligned")
    print(f"Optional Paths: {optional_present}/{optional_count} present")
    
    print(f"\nIndependent Verification Performed: ❌ NO")
    print(f"Verification Status: LOCAL FILESYSTEM CHECK ONLY")
    
    print("\n" + "="*80)
    
    if required_aligned:
        print("\n🚀 RESULT: WORKSPACE CONFIGURATION READY FOR EXECUTION")
        print("   All critical paths verified. Safe to proceed.\n")
        return 0
    else:
        print("\n⚠️  RESULT: WORKSPACE MISALIGNED - RESOLVE PATHS BEFORE GIT ACCESSION")
        print("   Missing critical files. Review above and deploy before continuing.\n")
        return 1

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    print("\n" + "*"*80)
    print("*" + " "*78 + "*")
    print("*" + " SCROLLVERSE WORKSPACE PATH VERIFIER v1.0.0 ".center(78) + "*")
    print("*" + " Zero Assumption // Maximum Transparency ".center(78) + "*")
    print("*" + " "*78 + "*")
    print("*"*80)
    
    exit_code = verify_workspace_alignment()
    sys.exit(exit_code)
