def FullOTA_InstallEnd(info):
	info.script.AppendExtra('symlink("/system/lib/libjhead.so", "/system/lib/libhead.so");')
	info.script.SetPermissionsRecursive("/system/UKM", 0, 0, 0755, 0755, None, None)
	info.script.MakeSymlinks((("/data/UKM/uci", "/system/xbin/uci"), ("/system/UKM/UKM","/system/etc/init.d/99UKM")))
	#info.script.AppendExtra('run_program("/sbin/make_ext4fs", "/dev/block/mmcblk0p9");')
