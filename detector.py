# ---------------------------------------------------------
# Copyright (c) 2026 Sbo3e. All rights reserved.
# Project: AI Ad-Fraud Detection System
# Domain: Security & Data Engineering
# ---------------------------------------------------------

import pandas as pd
import numpy as np

class Sbo3eSecurityEngine:
    def __init__(self):
        print("Sbo3e AI Security Engine is Active...")

    def detect_fraud(self, user_activity):
        """
        تحليل الأنماط لكشف الحسابات المشبوهة
        """
        df = pd.DataFrame(user_activity)
        
        # ميزة 1: كشف النقرات السريعة جداً (سلوك البوتات)
        # إذا ضغط المستخدم أكثر من 5 مرات في ثانية واحدة، يعتبر مشبوه
        fraud_flags = df.groupby('user_id').agg(
            click_count=('event_type', 'count'),
            unique_ips=('ip_address', 'nunique')
        )
        
        # معيار Sbo3e لكشف الاحتيال
        fraud_flags['is_bot'] = (fraud_flags['click_count'] > 5) | (fraud_flags['unique_ips'] > 3)
        
        return fraud_flags[fraud_flags['is_bot'] == True]

# --- بيانات تجريبية لمحاكاة الهجوم ---
activity_data = [
    {"user_id": "real_user_1", "event_type": "click", "ip_address": "1.1.1.1"},
    {"user_id": "bot_hacker_99", "event_type": "click", "ip_address": "2.2.2.2"},
    {"user_id": "bot_hacker_99", "event_type": "click", "ip_address": "2.2.2.3"},
    {"user_id": "bot_hacker_99", "event_type": "click", "ip_address": "2.2.2.4"},
    {"user_id": "bot_hacker_99", "event_type": "click", "ip_address": "2.2.2.5"},
    {"user_id": "bot_hacker_99", "event_type": "click", "ip_address": "2.2.2.6"},
    {"user_id": "bot_hacker_99", "event_type": "click", "ip_address": "2.2.2.7"},
]

engine = Sbo3eSecurityEngine()
suspicious_accounts = engine.detect_fraud(activity_data)

print("\n[ALERT] Sbo3e Detected Potential Fraud Accounts:")
print(suspicious_accounts)
