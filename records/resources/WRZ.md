---
records:
    - id: WRZHXTNHYH
      kind: problem-set
      title: Kvant 2014, no. 3
      creators:
        - name: Kvant editorial board
          role: editor
      date: "2014"
      msc:
        - code: 00A07
          from: kvant
        - code: 97U40
          from: kvant
      expressions:
        - key: e1
          kind: edition
          language: ru
          date: "2014"
          structure: WRZHXTNHYH/e1.json
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
          native_id: 2014-3
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
    - id: WRZVTKH240
      kind: monograph
      title: Spectral Theory of Non-Self-Adjoint Two-Point Differential Operators
      creators:
        - name: John Locker
          role: author
      date: "1999-10-26"
      msc:
        - code: 47A10
          from: zbmath_search
        - code: 47-02
          from: zbmath_search
        - code: 34L05
          from: zbmath_search
        - code: 47A75
          from: zbmath_search
        - code: "47E05"
          from: zbmath_search
        - code: 34-02
          from: zbmath_search
        - code: 34B27
          from: zbmath_search
        - code: 34L10
          from: zbmath_search
        - code: 34L20
          from: zbmath_search
        - code: 47A53
          from: zbmath_search
        - code: 47A70
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1999-10-26"
          ids:
            doi: 10.1090/surv/073
            zbl: "0945.47004"
            zbl_id: "1377488"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "1999-10-26"
              ids:
                isbn:
                    - "9780821820490"
                    - "9781470413002"
              access:
                class: record
      relations:
        - kind: part_of
          to: M891DMMNP3
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/surv/073
          level: work
        - source: crossref_language
          snapshot: blake3:fd7cbc47dac294e4452ea800fd3ae53f852825bb624f15dc020fcbd89fca6c56
          native_id: 10.1090/surv/073
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "1377488"
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
