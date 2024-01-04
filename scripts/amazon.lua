{"meta_name":"Amazon"}

browseto("https://www.amazon.fr/")
clickon("#nav-link-accountList-nav-line-1")
fill("#ap_email", meta_get("number"))
clickon("#continue")

if checkfor("#auth-error-message-box > div > h4") then
    meta_return(false)
else
    meta_return(true)
end

