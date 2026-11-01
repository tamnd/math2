---
records:
    - id: K8J6RYTTPV
      kind: problem-set
      title: Kvant 2008, no. 1
      creators:
        - name: Kvant editorial board
          role: editor
      date: "2008"
      msc:
        - code: 00A07
          from: kvant
        - code: 97U40
          from: kvant
      expressions:
        - key: e1
          kind: edition
          language: ru
          date: "2008"
          structure: K8J6RYTTPV/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 2008-1
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
    - id: K8JCFZGA6C
      kind: edited-volume
      title: Theory and Applications of Finite Fields
      creators:
        - name: Michel Lavrauw
          role: editor
        - name: Gary Mullen
          role: editor
        - name: Svetla Nikova
          role: editor
        - name: Daniel Panario
          role: editor
        - name: Leo Storme
          role: editor
      date: "2012"
      msc:
        - code: 00B25
          from: zbmath_search
        - code: 11-06
          from: zbmath_search
        - code: 11Gxx
          from: zbmath_search
        - code: 11Txx
          from: zbmath_search
        - code: 14G15
          from: zbmath_search
        - code: 51Exx
          from: zbmath_search
        - code: 94A60
          from: zbmath_search
        - code: 94Bxx
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2012"
          ids:
            doi: 10.1090/conm/579
            zbl: "1253.00023"
            zbl_id: "6110443"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2012"
              ids:
                isbn:
                    - "9780821852989"
                    - "9780821891575"
                    - "9780821891582"
              access:
                class: record
      relations:
        - kind: part_of
          to: VAEN3CBGT1
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/conm/579
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "6110443"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
    - id: K8JMTRS42G
      kind: preprint
      title: Sampling discretization of the uniform norm for hyperbolic-cross trigonometric polynomials
      creators:
        - name: Feng Dai
          role: author
        - name: Andriy Prymak
          role: author
      date: "2026-10-06"
      msc:
        - code: 65-XX
          from: arxiv
        - code: 26-XX
          from: arxiv
        - code: 46-XX
          from: arxiv
        - code: 60-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.NA
        - system: arxiv
          code: cs.NA
        - system: arxiv
          code: math.CA
        - system: arxiv
          code: math.FA
        - system: arxiv
          code: math.PR
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2026-10-06"
          ids:
            arxiv: "2610.07679"
            zbl_id: "903200196"
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.07679"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2610.07679"
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "903200196"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
