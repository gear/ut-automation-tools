# ut-automation-tools
Tools to automate bureaucracy shits at UT.

Tools available:
- `srwtimerec`: Clock in and clock out from the timestamp system.
```
30 8 * * 1,2,3,4,5 /home/gear/miniconda3/envs/dev/bin/python /home/gear/projects/ut-automation-tools/srwtimerec.py <staff_id> <staff_pw> in
5 17 * * 1,2,3,4,5 <path_to_python_env_bin>/python <path_to_this_proj>/srwtimerec.py <staff_id> <staff_pw> out
```

TODOs:
- [x] Add `crontab` configs.
- [] (Alternative to `cron`) Add Timer configs.
- [] Confirmation of successful stamps.
