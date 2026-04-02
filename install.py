import os
import subprocess
import shutil
import sys

def check_command(command):
    """檢查指令是否存在"""
    return shutil.which(command) is not None

def install():
    print("🚀 开始安装 web-to-notebook 技能...")

    # 1. 检查依赖
    deps = ["curl", "fabric-ai"]
    missing = [d for d in deps if not check_command(d)]

    if missing:
        print(f"⚠️  检测到缺失依赖: {', '.join(missing)}")
        print("💡 请先运行以下指令安装:")
        if "curl" in missing:
            print("   - sudo apt install curl (Debian/Ubuntu) 或 sudo pacman -S curl (Arch)")
        if "fabric-ai" in missing:
            print("   - pipx install fabric-ai 或 pip install fabric-ai")
        sys.exit(1)

    # 2. 检查 Fabric 配置
    print("✅ 基础依赖检查通过。")
    if not os.path.exists(os.path.expanduser("~/.config/fabric")):
        print("⚠️  检测到 Fabric 尚未初始化。")
        print("💡 请先运行 `fabric-ai --setup` 并配置您的 API Key。")
    
    # 3. 部署技能目录
    skill_src = "SKILL.md"
    skill_dest_dir = os.path.expanduser("~/.gemini/skills/web-to-notebook/")
    
    if not os.path.exists(skill_src):
        print(f"❌ 找不到源文件 {skill_src}，请确保在仓库目录下运行。")
        sys.exit(1)

    os.makedirs(skill_dest_dir, exist_ok=True)
    shutil.copy(skill_src, os.path.join(skill_dest_dir, "SKILL.md"))
    
    print(f"🎉 技能已成功部署至: {skill_dest_dir}")
    print("\n💡 使用方法:")
    print("   对 Gemini CLI 说: '激活 web-to-notebook，处理 https://example.com'")

if __name__ == "__main__":
    install()
