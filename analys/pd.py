import pandas as pd
import matplotlib.pyplot as plt

# Örnek veri seti
veri = {
    'İl': ['Ankara', 'Ankara', 'Ankara', 'İstanbul', 'İstanbul', 'İstanbul', 'İstanbul', 'İzmir', 'İzmir', 'İzmir'],
    'Üniversite': ['Uni1', 'Uni2', 'Uni3', 'Uni4', 'Uni5', 'Uni6', 'Uni7', 'Uni8', 'Uni9', 'Uni10'],
    'Kız_Sayısı': [500, 700, 800, 600, 900, 1000, 1100, 400, 600, 700],
    'Erkek_Sayısı': [700, 900, 1000, 800, 1200, 1300, 1400, 500, 800, 900]
}

# Veri setini DataFrame'e dönüştürme
df = pd.DataFrame(veri)

# Toplam öğrenci sayısını hesaplama
df['Toplam_Sayı'] = df['Kız_Sayısı'] + df['Erkek_Sayısı']

# Her bir il için ayrı ayrı kız ve erkek öğrenci sayılarını gösteren pembe ve mavi histogramlar oluşturma
fig, axes = plt.subplots(nrows=len(df['İl'].unique()), ncols=3, figsize=(15, 10))

for i, il in enumerate(df['İl'].unique()):
    il_veri = df[df['İl'] == il]
    
    if not il_veri.empty:
        il_veri.plot(kind='bar', x='Üniversite', y=['Kız_Sayısı', 'Erkek_Sayısı'], ax=axes[i, 0], color=['pink', 'lightblue'])
        axes[i, 0].set_title(f'{il} İli Öğrenci Sayıları')
        axes[i, 0].set_ylabel('Öğrenci Sayısı')
        axes[i, 0].tick_params(axis='x', rotation=45)
        axes[i, 0].legend(['Kız', 'Erkek'])
        
        il_veri.plot(kind='bar', x='Üniversite', y='Toplam_Sayı', ax=axes[i, 1], color='purple')
        axes[i, 1].set_title(f'{il} İli Toplam Öğrenci Sayısı')
        axes[i, 1].set_ylabel('Toplam Öğrenci Sayısı')
        axes[i, 1].tick_params(axis='x', rotation=45)
    
# Tüm illerdeki toplam kız ve erkek öğrenci sayılarını gösteren histogram
df_toplam = df.groupby('İl').sum()
df_toplam.plot(kind='bar', y=['Kız_Sayısı', 'Erkek_Sayısı'], ax=axes[0, 2], color=['pink', 'lightblue'])
axes[0, 2].set_title('Toplam Kız ve Erkek Öğrenci Sayıları')
axes[0, 2].set_ylabel('Öğrenci Sayısı')
axes[0, 2].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
