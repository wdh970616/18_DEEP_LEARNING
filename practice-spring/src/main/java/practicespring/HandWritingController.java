package practicespring;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.*;
import practicespring.dto.RequestDTO;
import practicespring.dto.ResponseDTO;

@RestController
@RequestMapping("/handwriting")
@RequiredArgsConstructor
@Slf4j
public class HandWritingController {

    private final WebClientService webClientService;

    @GetMapping("/test")
    public String test() {
        log.info("/test -> get 요청 테스트 들어옴");
        return "test success";
    }

    @PostMapping("/webclient")
    public ResponseDTO handwritingByWebClient(@RequestBody RequestDTO requestDTO) {

        log.info("손글씨 변환 Controller 요청 들어옴");
        log.info("handwriting: {}", requestDTO.getHandWriting());

        ResponseDTO generated_text = webClientService.handwritingToText(requestDTO);

        return generated_text;
    }
}
