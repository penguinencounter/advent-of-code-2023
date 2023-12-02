-- Hello from Lua! Please pipe in the input!

---@type string
local ln = io.read()

---Count the maximum value in a capture group across an entire string.
---@param source string
---@param match string
---@return integer
local function collect(source, match)
    local counter = 0
    for value in source:gmatch(match) do
        local p = tonumber(value) --[[@as integer]]
        if p > counter then
            counter = p
        end
    end
    return counter
end

local total = 0
while ln and ln ~= "" do
    if collect(ln, "(%d+) red") > 12 then
        goto continue
    end
    if collect(ln, "(%d+) green") > 13 then
        goto continue
    end
    if collect(ln, "(%d+) blue") > 14 then
        goto continue
    end
    do
        local id = ln:match("^Game (%d+)")
        total = total + tonumber(id)
    end
    ::continue::
    ln = io.read()
end
print(total)
