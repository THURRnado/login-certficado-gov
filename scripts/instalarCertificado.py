import os
import subprocess

CERTIFICADO_PATH = os.path.abspath("../auth/3S SOLUCOES CONTABEIS S_S LTDA_10587724000137.pfx")
SENHA_PATH = os.path.abspath("../auth/senha.txt")

# Lê a senha
with open(SENHA_PATH, 'r') as f:
    senha = f.read().strip()

print("🔧 Instalando certificado no Windows...")
print(f"📁 Arquivo: {CERTIFICADO_PATH}")

# Comando PowerShell para instalar o certificado
comando = f'''
$pwd = ConvertTo-SecureString -String "{senha}" -Force -AsPlainText
Import-PfxCertificate -FilePath "{CERTIFICADO_PATH}" -CertStoreLocation Cert:\\CurrentUser\\My -Password $pwd
'''

try:
    # Executa o PowerShell
    resultado = subprocess.run(
        ["powershell", "-Command", comando],
        capture_output=True,
        text=True
    )
    
    if resultado.returncode == 0:
        print("✅ Certificado instalado com sucesso!")
        print("\n💡 Agora você pode usar o certificado sem configurações extras no código.")
        print("💡 O Chrome detectará automaticamente quando o site solicitar.")
    else:
        print("❌ Erro ao instalar:")
        print(resultado.stderr)
        
except Exception as e:
    print(f"❌ Erro: {e}")