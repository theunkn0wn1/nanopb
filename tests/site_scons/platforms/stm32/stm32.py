# Compiler settings for running the tests on a STM32 discovery board
# Tested on the STM32F7 Discovery, but should work on pretty much
# any STM32 with >= 128kB of RAM. To avoid wearing out the flash,
# code is run from RAM also.

def set_stm32_platform(env):
    env.Replace(EMBEDDED = "1")
    env.Replace(CC  = "arm-none-eabi-gcc",
                CXX = "arm-none-eabi-g++",
                LD  = "arm-none-eabi-gcc")
    env.Replace(TEST_RUNNER = "site_scons/platforms/stm32/run_test.sh")
    env.Append(CFLAGS = "-mcpu=cortex-m3 -mthumb")
    env.Append(CXXFLAGS = "-mcpu=cortex-m3 -mthumb")
    env.Append(LINKFLAGS = "-mcpu=cortex-m3 -mthumb")
    env.Append(LINKFLAGS = "site_scons/platforms/stm32/vectors.c")
    env.Append(LINKFLAGS = "--specs=rdimon.specs --specs=nano.specs")
    env.Append(LINKFLAGS = "-Tsite_scons/platforms/stm32/stm32_ram.ld")
    
