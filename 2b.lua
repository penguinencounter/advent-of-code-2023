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
    local r = collect(ln, "(%d+) red")
    local g = collect(ln, "(%d+) green")
    local b = collect(ln, "(%d+) blue")
    total = total + r * g * b
    ln = io.read()
end
print(total)
