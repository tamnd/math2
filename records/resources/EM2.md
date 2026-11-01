---
records:
    - id: EM2J0ET9FG
      kind: problem-set
      title: Kvant 1991, no. 1
      creators:
        - name: Kvant editorial board
          role: editor
      date: "1991"
      msc:
        - code: 00A07
          from: kvant
        - code: 97U40
          from: kvant
      expressions:
        - key: e1
          kind: edition
          language: ru
          date: "1991"
          structure: EM2J0ET9FG/e1.json
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
          native_id: 1991-1
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
    - id: EM2J9TR22Q
      kind: monograph
      title: Invitation to Ergodic Theory
      creators:
        - name: C. Silva
          role: author
      date: "2007-12-18"
      msc:
        - code: 37-01
          from: zbmath_search
        - code: 28-01
          from: zbmath_search
        - code: 37Axx
          from: zbmath_search
        - code: 28Dxx
          from: zbmath_search
        - code: 37B05
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2007-12-18"
          ids:
            doi: 10.1090/stml/042
            zbl: "1151.37001"
            zbl_id: "5227136"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2007-12-18"
              ids:
                isbn:
                    - "9781470421519"
                    - "9780821884621"
                    - "9780821887332"
                    - "9780821844205"
              access:
                class: record
      relations:
        - kind: part_of
          to: 6RX4VMGQKK
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/stml/042
          level: work
        - source: crossref_language
          snapshot: blake3:78a08c6dff20a47d6ad06a8fc0424f997c851421644ee012bc0f425814d0a6d5
          native_id: 10.1090/stml/042
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "5227136"
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
          by: m2 v0.6.14 scope/1
          note: from in to in
---
