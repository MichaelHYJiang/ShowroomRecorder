基本要求：
	配置好ffmpeg，保证命令行中直接输入ffmpeg并回车以后能够出现以下内容：
		Use -h to get full help or, even better, run 'man ffmpeg'
	配置好python
	如果需要可以自己配置python虚拟环境，如果不了解虚拟环境可以不管
	用以下命令安装you-get
		python -m pip install you-get


录播步骤：
	1. 打开命令行窗口
		Windows平台打开方法：
			打开开始菜单
			输入cmd，回车（或者打开“命令提示符”）
		Mac：
			搜索“终端”或“Terminal”打开命令行窗口
		Linux：
			与Mac类似，或按WinKey -> 输入“终端”或“Terminal”-> 回车或点击对应图标

	2. 在命令行窗口中，通过cd命令到解压/下载的位置（cd命令的使用可以上网查，例子：“cd D:\\ChiyaHime\\Live”）；
	
	3. 直播开始后在命令行窗口中运行下面命令：
		python showroom_recorder.py --url https://www.showroom-live.com/tsukishiro_chiya --name Chiya

	    --url 后面的部分指定录播房间
	    --name 指定保存文件的文件名后缀
	
	4. 直播结束后如果长时间未停止，可按Ctrl + C停止；
	
	5. 直播中途如因为网络连接不好程序中断运行，可以重新运行3中的指令，继续录播；

	6. 生成的文件会以“yyyy-mm-dd_hh-nn-ss_Chiya_.mp4”命名，yyyy-mm-dd_hh-nn-ss表示开始录制时的年月日时分秒；

	7. 运行过程中会生成一个you-get_info_temp文件，不会很大，请无视。运行完以后可以随意删除。

