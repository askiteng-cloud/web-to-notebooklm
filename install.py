import os
import shutil
import sys

def check_command(command):
    """檢查指令是否存在"""
    return shutil.which(command) is not None

def install():
    print("🚀 開始安裝 Web-to-NotebookLM 技能...")

    # 1. 檢查依賴
    deps = ["curl", "fabric-ai"]
    missing = [d for d in deps if not check_command(d)]

    if missing:
        print(f"⚠️  檢測到缺失依賴: {', '.join(missing)}")
        if "fabric-ai" in missing:
            print("💡 請前往安裝 Fabric-AI: https://github.com/danielmiessler/Fabric")
        else:
            print("💡 請先安裝依賴項。")
        sys.exit(1)

    # 2. 定義安裝路徑
    skill_src = "SKILL.md"
    skill_name = "web-to-notebooklm"
    
    # 潛在的安裝目標
    targets = [
        os.path.expanduser(f"~/.gemini/skills/{skill_name}/"),
        os.path.expanduser(f"~/.openclaw/skills/{skill_name}/")
    ]

    if not os.path.exists(skill_src):
        print(f"❌ 找不到源文件 {skill_src}。")
        sys.exit(1)

    installed_paths = []
    for dest_dir in targets:
        # 建立目錄並拷貝
        os.makedirs(dest_dir, exist_ok=True)
        shutil.copy(skill_src, os.path.join(dest_dir, "SKILL.md"))
        installed_paths.append(dest_dir)
        print(f"✅ 已部署至: {dest_dir}")

    print(f"\n🎉 技能安裝完成！")
    print("\n💡 使用方法:")
    print(f"   - Gemini CLI: 'web-to-notebooklm, 處理 https://example.com'")
    print(f"   - OpenClaw (IM): '脫水 https://example.com'")

if __name__ == "__main__":
    install()
