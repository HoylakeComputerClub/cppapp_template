workspace "hcc"
	startproject "cppproject"
	architecture "x64"

	configurations
	{
		"Debug",
		"Release"
	}

project "cppproject"
	location "cppproject"
	kind "ConsoleApp"
	language "C++"
	cppdialect "C++17"

	files
	{
		"%{prj.name}/src/**.hpp",
		"%{prj.name}/src/**.cpp"
	}

	flags
	{
		"FatalWarnings"
	}
