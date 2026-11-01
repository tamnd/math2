---
records:
    - id: MP7GA6MQED
      kind: preprint
      title: BKT transition for $\mathsf{Sine}_\beta$
      creators:
        - name: Theodoros Assiotis
          role: author
      date: "2026-10-09"
      msc:
        - code: 60-XX
          from: arxiv
        - code: 81-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.PR
        - system: arxiv
          code: math-ph
        - system: arxiv
          code: math.MP
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2026-10-09"
          ids:
            arxiv: "2610.13484"
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.13484"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2610.13484"
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
    - id: MP7J9P010R
      kind: monograph
      title: 'Rational Number Theory in the 20th Century: From PNT to FLT'
      creators:
        - name: Władysław Narkiewicz
          role: author
      date: "2012"
      msc:
        - code: 11-02
          from: zbmath_search
        - code: 11-03
          from: zbmath_search
        - code: 11-00
          from: zbmath_search
        - code: 01A60
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2012"
          ids:
            doi: 10.1007/978-0-85729-532-3
            zbl: "1230.11001"
            zbl_id: "5898722"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer London
              date: "2012"
              ids:
                isbn:
                    - "9780857295316"
                    - "9780857295323"
              access:
                class: record
      relations:
        - kind: part_of
          to: FA5PXCH6G7
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-0-85729-532-3
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "5898722"
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
---
