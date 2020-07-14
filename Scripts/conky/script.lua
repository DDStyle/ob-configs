requre 'cairo'

function conky_main()
	 local updates = tonumber (conky_parse ('${updates}'))
    if updates > 5 then
        print ("hello world")
    end
end