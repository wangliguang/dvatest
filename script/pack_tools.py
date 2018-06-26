
def get_build(version):
    nums = version.split('.')
    if len(nums) < 3:
        print 'version format check error'
        return '0'

    for i in range(0, 2):
        num = nums[i]
        if not num.isdigit():
            print 'version number check error'
            return '0'

    nums[1] = '0' if int(nums[1]) < 0 else nums[1]
    nums[2] = '0' if int(nums[2]) < 0 else nums[2]

    result = nums[0]
    result += '0' if int(nums[1]) < 10 else ''
    result += nums[1]
    result += '0' if int(nums[2]) < 10 else ''
    result += nums[2]

    return result
