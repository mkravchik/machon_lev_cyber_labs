echo "enter your username in JCT"
read Uname
cp ~/.bashrc ~/.bashrc.bak
echo export PS1="$Uname:$">> ~/.bashrc
export PS1="$Uname:$"
echo "✅ Prompt changed successfully. Restart your shell or run 'source ~/.bashrc' to apply changes."

