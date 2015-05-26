def FullOTA_InstallEnd(info):
	info.script.AppendExtra('symlink("/system/lib/libjhead.so", "/system/lib/libhead.so");')
	info.script.SetPermissionsRecursive("/system/UKM", 0, 0, 0755, 0755, None, None)
	info.script.MakeSymlinks((("/data/UMK/uci", "/system/xbin/uci"), ("/system/UMK/UMK","/system/etc/init.d/99UMK")))
	#info.script.AppendExtra('run_program("/sbin/make_ext4fs", "/dev/block/mmcblk0p9");')
