import pandas as pd
import numpy as np

df_admission = pd.read_csv("dataset/ADMISSION.csv")
df_baseline = pd.read_csv("dataset/BASELINE_CLIN.csv")
df_biology = pd.read_csv("dataset/BIOLOGY.csv")
df_inclusion = pd.read_csv("dataset/INCLUSION.csv")
df_kydney = pd.read_csv("dataset/KIDNEY_FAILURE.csv")
df_nosocomial = pd.read_csv("dataset/NOSOCOMIAL.csv")
df_randomization = pd.read_csv("dataset/RANDOMIZATION.csv")
df_sofa = pd.read_csv("dataset/SOFA.csv")
df_vital = pd.read_csv("dataset/VITAL_STATUS.csv")

print(df_admission.head())




