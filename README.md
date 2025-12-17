# Forward Only - 一款第一人称记忆探索游戏

一个基于Three.js的沉浸式3D游戏体验，探索楼梯上的记忆碎片。

## 🎮 游戏玩法

- **自动前进**：游戏开始后，你会自动向前移动穿过无尽的楼梯
- **观察记忆**：墙壁上会出现"裂缝"，凝视它们可以显示记忆图像
- **平衡速度**：越盯着记忆看，身后的楼梯崩塌得越快
- **生存挑战**：不要让楼梯在你脚下完全崩塌！

## 🚀 快速开始

### 方法1：直接打开HTML文件

1. 下载所有文件
2. 在浏览器中打开 `index.html`
3. 点击"START"按钮开始游戏

### 方法2：使用本地服务器（推荐）

```bash
# Python 3
python3 -m http.server 8000

# 或者使用 Python 2
python -m SimpleHTTPServer 8000

# 然后在浏览器打开
# http://localhost:8000
```

### 方法3：使用 Node.js

```bash
# 安装 http-server
npm install -g http-server

# 运行服务器
http-server -p 8000

# 在浏览器打开
# http://localhost:8000
```

## 🎯 游戏控制

- **鼠标移动**：环顾四周
- **凝视**：将准星对准墙上的裂缝，凝视以显示记忆
- **ESC**：退出锁定模式

## 📸 自定义图片

游戏会显示 `images/` 文件夹中的20张图片（memory01.jpg - memory20.jpg）。

### 更换自己的图片：

1. 准备20张 JPG 格式的图片
2. 命名为 `memory01.jpg`, `memory02.jpg`, ..., `memory20.jpg`
3. 放入 `images/` 文件夹

### 重新生成示例图片：

```bash
python3 generate_images.py
```

## 🛠️ 技术栈

- **Three.js r128** - 3D 渲染引擎
- **原生 JavaScript** - 游戏逻辑
- **HTML5 Canvas** - 图像处理和特效
- **Pointer Lock API** - 第一人称控制

## 📁 文件结构

```
.
├── index.html           # 主游戏文件
├── images/              # 记忆图片文件夹
│   ├── memory01.jpg
│   ├── memory02.jpg
│   └── ...
├── generate_images.py   # 图片生成脚本
└── README.md           # 说明文档
```

## ⚙️ 游戏参数调整

你可以在 `index.html` 中修改 `SETTINGS` 对象来调整游戏体验：

```javascript
const SETTINGS = {
  baseSpeed: 4.4,           // 基础移动速度
  lookSlowMax: 0.55,        // 观看时的最大减速
  decayBasePerSec: 2.2,     // 基础崩塌速度
  decayBoostPerSec: 6.5,    // 观看时的崩塌加速
  fissureEveryN: 7,         // 每N个台阶出现一个裂缝
  // ... 更多设置
};
```

## 🌐 在线部署

### GitHub Pages

1. 上传所有文件到 GitHub 仓库
2. 进入仓库设置 → Pages
3. 选择分支并保存
4. 访问 `https://yourusername.github.io/repository-name`

### Netlify / Vercel

直接将整个文件夹拖放到这些平台即可部署。

## 🎨 游戏特色

- **动态视觉反馈**：随着压力增加，视野会收缩，晕影效果增强
- **程序化内容**：每个裂缝的形状和位置都是独特的
- **性能优化**：智能流式加载和卸载楼梯，保持流畅运行
- **沉浸式体验**：雾效、光照和音频反馈创造紧张氛围

## 📝 许可证

此项目仅供学习和个人使用。

## 🤝 贡献

欢迎提交问题和改进建议！

---

**享受游戏！记住：不要盯着记忆看太久... ⚠️**
