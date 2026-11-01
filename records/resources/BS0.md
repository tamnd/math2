---
records:
    - id: BS03TBEF03
      kind: problem-set
      title: Kvant 1979, no. 7
      creators:
        - name: Kvant editorial board
          role: editor
      date: "1979"
      msc:
        - code: 00A07
          from: kvant
        - code: 97U40
          from: kvant
      expressions:
        - key: e1
          kind: edition
          language: ru
          date: "1979"
          structure: BS03TBEF03/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 1979-7
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
    - id: BS0QDYQ50E
      kind: monograph
      title: Algebraic Ideas in Ergodic Theory
      creators:
        - name: Klaus Schmidt
          role: author
      date: "1990-10-09"
      msc:
        - code: 28D05
          from: zbmath_search
        - code: 28-02
          from: zbmath_search
        - code: 28D15
          from: zbmath_search
        - code: 28D20
          from: zbmath_search
        - code: 54C70
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1990-10-09"
          ids:
            doi: 10.1090/cbms/076
            zbl: "0719.28006"
            zbl_id: "48085"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "1990-10-09"
              ids:
                isbn:
                    - "9780821807279"
                    - "9780821889206"
                    - "9781470424367"
              access:
                class: record
      relations:
        - kind: part_of
          to: 20XHFD4A67
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/cbms/076
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "48085"
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
