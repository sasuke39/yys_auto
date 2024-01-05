<div align="center">

<br><br>

# OnmyojiAutoScript

<br>

<div>
    <img alt="python" src="https://img.shields.io/badge/python-3.10-%233776AB?logo=python">
</div>
<div>
    <img alt="platform" src="https://img.shields.io/badge/platform-Windows-blueviolet">
</div>
<div>
    <img alt="license" src="https://img.shields.io/github/license/runhey/OnmyojiAutoScript">
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/runhey/OnmyojiAutoScript">
    <img alt="GitHub all releases" src="https://img.shields.io/github/downloads/runhey/OnmyojiAutoScript/total">
    <img alt="stars" src="https://img.shields.io/github/stars/runhey/OnmyojiAutoScript?style=social">
</div>
<br>

阴阳师 自动化 脚本 

基于图像识别技术，一键托管

绝赞更新中✿✿ヽ(°▽°)ノ✿<br>

### [文档](https://runhey.github.io/OnmyojiAutoScript-website/)

</div>


## 功能 Features

- OAS 还在开发中，[查看已实现](https://github.com/runhey/OnmyojiAutoScript/issues/54)

### 显著特点 

## 许可证 LICENSE

This project is licensed under the GNU General Public License v3.0.

## 声明 Announcement
本软件开源、免费，仅供学习交流使用。开发者团队拥有本项目的最终解释权。使用本软件产生的所有问题与本项目与开发者团队无关。

## 相关项目 Relative Repositories
- [Alas](https://github.com/LmeSzinc/AzurLaneAutoScript): 碧蓝航线的自动化脚本，OAS 在其架构上开发
- [SRC](https://github.com/LmeSzinc/StarRailCopilot): 崩坏：星穹铁道脚本，基于下一代Alas框架
- [OAS-website](https://github.com/runhey/OnmyojiAutoScript-website): OAS 的文档网站，使用 [docusaurus](https://docusaurus.io/) 构建
- [FluentUI](https://github.com/zhuzichu520/FluentUI): GUI 库，使用 QML 语言
- [Uowl](https://github.com/runhey/Uowl): 作者早期的 Onmyoji 脚本，已停止维护
- [ppocr-onnx](https://github.com/triwinds/ppocr-onnx): OCR 库，基于 onnxruntime 和 PaddleOCR
- [gurs](https://github.com/2833844911/gurs): 基于赛贝尔曲线模拟滑动轨迹

## 联系/加入我们 Contact/Join Us

#### QQ交流群: 465946275

相对于其他的游戏，阴阳师玩家总体而言对脚本这类工具具有极高的排斥性。树大招风，无论你是否喜欢 OAS ，我们都希望你不在互联网上进行宣传，这保护 OAS , 也保护开发者们。

为此保持较高的入群门槛:  
- 你的QQ等级必须大于32级(🌞🌞)，注册时间超过一年，低等级账号成分复杂，还请见谅。
- 你必须拥有一个 Github 账户来点一个 **Star** (这并不影响你入群后取消Star)，同样的要求注册时间过半年。
- 入群验证填入你的 Github 账号名，无需在意问题是什么。

#### QQ开发群: 207613181

- 发展规划：[#54](https://github.com/runhey/OnmyojiAutoScript/issues/54)
- OAS 继承了 Alas 的设计思路，这使得极大简便了开发，欢迎提交 Pull Requests，挑选你感兴趣的部分进行开发即可。
- OAS 仍在活跃中， 我们会不定期发布未来的工作在 Issues 上并标记为 `help wanted`，欢迎向 OAS 提交 Pull Requests，我们会认真阅读你的每一行代码的。

## 鸣谢 Acknowledgements

感谢所有参与到开发/测试中的朋友们

[![Contributors](https://contributors-img.web.app/image?repo=runhey/OnmyojiAutoScript)](https://github.com/runhey/OnmyojiAutoScript/graphs/contributors)

感谢所有完善文档的朋友们

[![Contributors](https://contributors-img.web.app/image?repo=runhey/OnmyojiAutoScript-website)](https://github.com/runhey/OnmyojiAutoScript-website/graphs/contributors)

<div align="center">

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=runhey/OnmyojiAutoScript&type=Date)](https://star-history.com/#runhey/OnmyojiAutoScript&Date)


## ⚡ Visitor count

![](https://profile-counter.glitch.me/runhey-OnmyojiAutoScript/count.svg)

</div>


执行任务流程，执行module.gui.context.process_manager.ProcessManager.start_script方法
该方法获取队形model的配置文件，然后获取下一个任务，执行任务
执行任务对应的Run方法，在script方法下面run()

如果新建一个任务，需要把任务添加到任务队列类，添加任务对应的run方法。
如何构建新的窗口 通过Model里的添加属性即刻 qt界面是即使生产的