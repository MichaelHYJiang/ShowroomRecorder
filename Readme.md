#Showroom Recorder



<!-- ABOUT THE PROJECT -->
## About The Project

A simple command-line tool to download source streams from [Showroom](https://www.showroom-live.com).

Although [You-Get](https://github.com/soimort/you-get) offers an easy way of downloading live streams, it has certain latencies on different machines under various network conditions, which could lead to package losses during Showroom recordings.

Thus, this project uses [You-Get](https://github.com/soimort/you-get) only to parse m3u8 playlist links, and download stream with ffmpeg directly to achieve a higher speed and more stability.



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites
* [FFmpeg](https://ffmpeg.org/)
* [You-Get](https://github.com/soimort/you-get)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/MichaelHYJiang/ShowroomRecorder.git
   ```



<!-- USAGE EXAMPLES -->
## Usage

1. Run command
    ```sh
    python showroom_recorder.py [--url URL] [-U URL] [--name NAME] [-N NAME]
    ```
2. Arguments

	*  -h, --help: show this help message and exit
	*  --url URL, -U URL: Specify room URL (Default is [Tsukishiro_chiya](https://www.showroom-live.com/tsukishiro_chiya)).
	*  --name NAME, -N NAME: Specify suffix name of the recored file (Default is "Chiya").
	*  --version, -V: show program's version number and exit

3. Examples
    ```sh
    python showroom_recorder.py
    python showromm_reocrder.py -U https://www.showroom-live.com/tsukishiro_chiya -N Chiya
    python showromm_reocrder.py --url https://www.showroom-live.com/576164216485 --name Yutoha
    ```

4. Results
	Recorded video will have its formatted starting time (`yyyy-mm-dd_hh-nn-ss`) as filename prefix, argument specified name as suffix, and mp4 as file extension.
    An intermediate file named "you-get_info_temp" will be generated during the parsing process, and can be removed after each run.
	It is safe to break at any time using `Ctrl+C`.


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.