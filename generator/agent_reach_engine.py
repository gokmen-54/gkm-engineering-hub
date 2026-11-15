"""
Agent Reach - Autonomous B2B Lead Radar & Outreach Engine for GKM Elektrik
Continuously detects industrial prospects, matches them with concrete case studies,
and keeps the outreach database ready for 1-click execution.
"""

import os
import json
import urllib.parse
import urllib.request
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE_PATH = os.path.join(BASE_DIR, "generator", "agent_reach_database.json")
SITE_URL = "https://muhendislik.gkmelektrik.com"

def ping_google_sitemap():
    sitemap_url = f"{SITE_URL}/sitemap.xml"
    ping_url = f"https://www.google.com/ping?sitemap={urllib.parse.quote(sitemap_url)}"
    try:
        req = urllib.request.Request(ping_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            status = response.getcode()
            print(f"[AGENT-REACH] Googlebot sitemap ping status: {status}")
            return True
    except Exception as e:
        print(f"[AGENT-REACH] Googlebot ping notice: {e}")
        return False

def sync_leads():
    if not os.path.exists(DATABASE_PATH):
        print("[AGENT-REACH] Database file not found!")
        return []
    
    with open(DATABASE_PATH, "r", encoding="utf-8") as f:
        leads = json.load(f)
    
    print(f"[AGENT-REACH] Active target leads count: {len(leads)}")
    for l in leads:
        print(f" -> [{l['sector_title']}] {l['company']} (Problem: {l['need'][:40]}...)")
    
    return leads

if __name__ == "__main__":
    print("=" * 60)
    print("🎯 GKM AGENT REACH - B2B INDUSTRIAL OUTREACH RADAR")
    print("=" * 60)
    sync_leads()
    ping_google_sitemap()
