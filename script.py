cd ~/bbingham/catkin_ws
EXTS=("*.py" "*.sh")
for EXT in "${EXTS[@]}"
do
  find . -type f -name ${EXT} -exec chmod +x "{}" \;
done
